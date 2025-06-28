from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.html import format_html

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'qr_preview')
    readonly_fields = ('qr_preview',)
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('qr_code', 'qr_preview')}),
    )

    def qr_preview(self, obj):
        if obj.qr_code and hasattr(obj.qr_code, 'url'):
            return format_html('<img src="{}" style="height:100px;"/>', obj.qr_code.url)
        return "-"

    qr_preview.short_description = "QR Code"

admin.site.register(CustomUser, CustomUserAdmin)
