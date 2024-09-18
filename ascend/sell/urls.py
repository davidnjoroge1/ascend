from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'sell'

urlpatterns = [
    path('', views.sell, name='sell'),
    path('delete-request/<int:request_id>/', views.delete_request, name='delete_request'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)