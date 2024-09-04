from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import password_changed
from django.core.serializers import serialize
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserLoginSerializer, UserRegisterSerializer, UserChangePasswordSerializer, UserSendResetPasswordEmailSerializer, UserPasswordResetSerializer
from rest_framework import viewsets
from .models import CustomUser
from django.contrib.auth import get_user_model
from .pagination import LimitOffsetPagination
from django.utils.encoding import force_str

User = get_user_model()

def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_token_for_user(user)
            return Response({'token': token, 'msg': 'Login Success'}, status=status.HTTP_200_OK)
        return Response({'errors': {'non_field_errors': ['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
class UserRegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_token_for_user(user)
        return Response({"token": token, 'msg': 'Registration Successfully'}, status=status.HTTP_201_CREATED)
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     # serializer_class = UserCreateSerializer()
#     pagination_class = LimitOffsetPagination


class UserChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserChangePasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={"user": request.user})
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Password changed successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserSendResetPasswordEmailView(APIView):
    serializer_class = UserSendResetPasswordEmailSerializer  # یہاں serializer_class کو بیان کریں
    permission_classes = [AllowAny,]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data['email']
            user = CustomUser.objects.filter(email=email).first()
            if user:
                token_generator = PasswordResetTokenGenerator()
                token = token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.id))
                reset_link = f"{request.build_absolute_uri('/reset-password/')}?uid={uid}&token={token}"
                send_mail(
                    'Password Reset Request',
                    f'Click on this link to reset your password: {reset_link}',
                    'azharkhanzada356@gmail.com',
                    [email],
                    fail_silently=False,
                )
                return Response({'msg': 'Password reset link has been sent to your email.'}, status=status.HTTP_200_OK)
            return Response({'errors': {'email': 'No user found with this email.'}}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserPasswordResetView(APIView):
    serializer_class = UserPasswordResetSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        uid = request.query_params.get('uid')
        token = request.query_params.get('token')
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(uid=uid, token=token)
            return Response({'msg': 'Password has been reset successfully.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
