from django.contrib import admin
from django.utils.html import format_html
from .models import InstagramBoostRequest, TikTokBoostRequest, YouTubeBoostRequest

@admin.register(TikTokBoostRequest)
class TikTokBoostRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'tiktok_username', 'follower_package', 'submitted_at', 'payment_screenshot_link')
    list_filter = ('follower_package', 'submitted_at')
    search_fields = ('user__username', 'tiktok_username')
    readonly_fields = ('submitted_at', 'payment_screenshot_link')

    def payment_screenshot_link(self, obj):
        if obj.payment_screenshot:
            return format_html('<a href="{}" target="_blank">View Screenshot</a>', obj.get_payment_screenshot_url())
        return "No screenshot"
    payment_screenshot_link.short_description = 'Payment Screenshot'
@admin.register(InstagramBoostRequest)
class InstagramBoostRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'instagram_username', 'follower_package', 'submitted_at', 'payment_screenshot_link')
    list_filter = ('follower_package', 'submitted_at')
    search_fields = ('user__username', 'instagram_username')
    readonly_fields = ('submitted_at', 'payment_screenshot_link')

    def payment_screenshot_link(self, obj):
        if obj.payment_screenshot:
            return format_html('<a href="{}" target="_blank">View Screenshot</a>', obj.get_payment_screenshot_url())
        return "No screenshot"
    payment_screenshot_link.short_description = 'Payment Screenshot'

@admin.register(YouTubeBoostRequest)
class YouTubeBoostRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'youtube_channel', 'boost_package', 'watch_hours', 'comment_boost', 'submitted_at', 'payment_screenshot_link')
    list_filter = ('boost_package', 'watch_hours', 'submitted_at')
    search_fields = ('user__username', 'youtube_channel')
    readonly_fields = ('submitted_at', 'payment_screenshot_link')

    def payment_screenshot_link(self, obj):
        if obj.payment_screenshot:
            return format_html('<a href="{}" target="_blank">View Screenshot</a>', obj.get_payment_screenshot_url())
        return "No screenshot"
    payment_screenshot_link.short_description = 'Payment Screenshot'

class SnapchatBoostAdmin(admin.ModelAdmin):
    list_display = ['user', 'username', 'follower_package', 'submission_date']
    list_filter = ['submission_date', 'follower_package']
