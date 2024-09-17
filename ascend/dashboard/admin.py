from django.contrib import admin
from .models import TikTokBoost, InstagramBoost, YouTubeBoost

@admin.register(TikTokBoost)
class TikTokBoostAdmin(admin.ModelAdmin):
    list_display = ('username', 'follower_package', 'submitted_at', 'is_processed')
    list_filter = ('follower_package', 'is_processed', 'submitted_at')
    search_fields = ('username',)
    readonly_fields = ('submitted_at',)

@admin.register(InstagramBoost)
class InstagramBoostAdmin(admin.ModelAdmin):
    list_display = ('username', 'follower_package', 'submitted_at', 'is_processed')
    list_filter = ('follower_package', 'is_processed', 'submitted_at')
    search_fields = ('username',)
    readonly_fields = ('submitted_at',)

@admin.register(YouTubeBoost)
class YouTubeBoostAdmin(admin.ModelAdmin):
    list_display = ('channel_url', 'subscriber_package', 'submitted_at', 'is_processed')
    list_filter = ('subscriber_package', 'is_processed', 'submitted_at')
    search_fields = ('channel_url',)
    readonly_fields = ('submitted_at',)