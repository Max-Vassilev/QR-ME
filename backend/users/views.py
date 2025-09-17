from rest_framework import generics, serializers
from rest_framework.permissions import AllowAny
from .models import CustomUser
import qrcode, os
from django.conf import settings

class UserSerializer(serializers.ModelSerializer):
    qr_code_url = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ["id", "username", "password", "qr_code_url"]
        extra_kwargs = {"password": {"write_only": True}}

    def get_qr_code_url(self, obj):
        request = self.context.get('request')
        if obj.qr_code and request:
            return request.build_absolute_uri(obj.qr_code.url)
        return None

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

def qr_code_generator(url, path):
    qrcode.make(url).save(path)

class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        url = f"http://54.160.207.170:5173/public/{user.username}"
        folder = os.path.join(settings.MEDIA_ROOT, "qr_codes")
        os.makedirs(folder, exist_ok=True)
        path = os.path.join(folder, f"{user.username}.png")
        qr_code_generator(url, path)
        user.qr_code.name = f"qr_codes/{user.username}.png"
        user.save()

class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def get_serializer_context(self):
        return {"request": self.request}
