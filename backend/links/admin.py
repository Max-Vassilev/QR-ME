from django.contrib import admin
from .models import Link

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('owner', 'platform', 'url', 'created_at')
    search_fields = ('platform', 'url', 'owner__username')
    list_filter = ('platform', 'created_at')
