from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from .models import CustomUser
# from .pagination import UserPagination
from rest_framework.pagination import LimitOffsetPagination

from .serializers import UserCreateSerializer
from .pagination import UserLimitOffsetPagination
# from .pagination import UserCursorPagination


class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer
    # pagination_class = UserPagination
    pagination_class = UserLimitOffsetPagination
    # pagination_class = UserCursorPagination


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

#
#
# from rest_framework import generics, viewsets
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth import get_user_model
# from .models import CustomUser
# from .serializers import UserCreateSerializer
# from .pagination import UserLimitOffsetPagination
#
# User = get_user_model()
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserCreateSerializer
#     pagination_class = UserLimitOffsetPagination
#
# class RegisterUserView(generics.CreateAPIView):
#     serializer_class = UserCreateSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({
#                 'username': user.username,
#                 'email': user.email,
#                 'phone_number': user.phone_number
#             }, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
