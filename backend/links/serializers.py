from rest_framework import serializers
from .models import Link

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ["id", "owner", "platform", "url", "created_at"]
        extra_kwargs = {"owner": {"read_only": True}}