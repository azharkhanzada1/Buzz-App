from django.urls import path
from .views import UserLoginView, UserRegisterView, UserChangePasswordView, UserSendResetPasswordEmailView, UserPasswordResetView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenRefreshView,TokenVerifyView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('change-password/', UserChangePasswordView.as_view(), name='change-password'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify_token/', TokenVerifyView.as_view(), name='token_verify'),
    path('send-forget-password/', UserSendResetPasswordEmailView.as_view(), name="send-forget-password"),
    path('reset-password/', UserPasswordResetView.as_view(), name='reset-password'),
]
