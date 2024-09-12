from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('buzz.urls')),
    path('', include('user.urls')),
    path('', include('follow.urls')),
    path('', include('notification.urls')),
]