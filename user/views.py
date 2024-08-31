from django.core.serializers import serialize
from rest_framework import generics, status, permissions
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import CustomUser
from .serializers import UserCreateSerializer
from .pagination import UserLimitOffsetPagination

class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer
    pagination_class = UserLimitOffsetPagination

@permission_classes([AllowAny])
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
                }, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)