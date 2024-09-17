from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('tiktok-boost/', views.tiktok_boost, name='tiktok_boost'),
    path('instagram-boost/', views.instagram_boost, name='instagram_boost'),
    path('youtube-boost/', views.youtube_boost, name='youtube_boost'),
    path('snapchat-boost/', views.snapchat_boost, name='snapchat_boost'),
    path('youtube-boost/', views.youtube_boost, name='youtube_boost'),
    path('media/<path:path>', views.serve_media, name='serve_media'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)