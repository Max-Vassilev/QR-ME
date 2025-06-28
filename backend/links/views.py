from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from rest_framework.exceptions import NotFound
from .serializers import LinkSerializer
from .models import Link

class LinkList(generics.ListAPIView):
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Link.objects.filter(owner=self.request.user)

class LinkCreate(generics.CreateAPIView):
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LinkDelete(generics.DestroyAPIView):
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Link.objects.filter(owner=self.request.user)

class PublicUserLinksView(generics.ListAPIView):
    serializer_class = LinkSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        username = self.kwargs.get('username')
        User = get_user_model()
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound("User not found")
        return Link.objects.filter(owner=user)
