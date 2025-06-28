from rest_framework import generics, serializers
from rest_framework.permissions import AllowAny
from .models import CustomUser
import qrcode, os

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "password", "qr_code"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

def qr_code_generator(url, filename):
    qrcode.make(url).save(filename)

class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        url = f"http://localhost:5173/public/{user.username}"
        filename = f"qr_codes/{user.username}.png"
        os.makedirs("qr_codes", exist_ok=True)
        qr_code_generator(url, filename)
        user.qr_code.name = f"qr_codes/{user.username}.png"
        user.save()
