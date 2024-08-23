# from os import access
#
# from django.contrib.auth.models import AbstractUser
# from django.core.serializers import serialize
# from rest_framework import status, generics
# from rest_framework.response import  Response
# from django.contrib.auth import get_user_model
# from rest_framework_simplejwt.tokens import RefreshToken
# from .serializers import  UserCreateSerializer, UserSerializer, TokenSerializer
#
# User = get_user_model()
#
# class RegisterUserView(generics.CreateAPIView):
#     serializer_class = UserCreateSerializer
#
# class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     lookup_field = 'username'
#
# class TokenObtainPairView(generics.GenericAPIView):
#     def post(self, request, *args, **kwargs):
#         serializer = TokenSerializer(data=request.data)
#         if serializer.is_valid():
#             refresh = RefreshToken.for_user(request.user)
#             data = {
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             }
#             return Response(data, status=status.HTTP_200_OK)
#         return Response(serialize.errors, status = status.HTTP_400_BAD_REQUEST)




from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializer

class RegisterUserView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'username': user.username,
                'email': user.email,
                'phone_number': user.phone_number
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

















# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from .models import CustomUser
# from .serializers import RegisterSerializer, UserSerializer
#
# class RegisterView(generics.CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = RegisterSerializer
#
# class UserProfileView(generics.RetrieveUpdateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get_object(self):
#         return self.request.user

