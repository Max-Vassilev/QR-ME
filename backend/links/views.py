from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import LinkSerializer
from .models import Link

class LinkList(generics.ListAPIView):
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Link.objects.filter(author=self.request.user)

class LinkCreate(generics.CreateAPIView):
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class LinkDelete(generics.DestroyAPIView):
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Link.objects.filter(author=self.request.user)
