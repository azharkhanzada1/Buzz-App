from django.urls import path, include
from rest_framework.routers import DefaultRouter
from notification.views import NotificationView

routers = DefaultRouter()
routers.register(r'notifications',  NotificationView)

urlpatterns = [
    path('notification/', include(routers.urls)),
]
