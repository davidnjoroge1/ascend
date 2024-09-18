from django.contrib import admin
from .models import SellRequest

@admin.register(SellRequest)
class SellRequestAdmin(admin.ModelAdmin):
    list_display = ('tiktokUsername', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('tiktokUsername', 'accountDescription')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('user', 'tiktokUsername', 'accountDescription', 'accountScreenshot', 'status')
        }),
        ('Admin Feedback', {
            'fields': ('admin_comments',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # You can add logic here to notify the user when admin updates the status or comments