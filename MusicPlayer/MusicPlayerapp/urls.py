from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static 

app_name = "MusicPlayerapp"

urlpatterns = [
    path('', views.index, name='index'),  # Map root URL to your view
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)