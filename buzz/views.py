from rest_framework import viewsets
from .models import Post, Comment, Like, View
from rest_framework.authentication import BaseAuthentication
from .serializers import PostSerializer, CommentSerializer, LikeSerializer, ViewSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # authentication_classes = [JWTAuthentication]
    # authentication_classes = [BaseAuthentication]
    permission_classes = [IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # authentication_classes = [JWTAuthentication]
    # authentication_classes = [BaseAuthentication]
    permission_classes = [IsAuthenticated]

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    # authentication_classes = [JWTAuthentication]
    # authentication_classes = [BaseAuthentication]
    permission_classes = [IsAuthenticated]

class ViewViewSet(viewsets.ModelViewSet):
    queryset = View.objects.all()
    serializer_class = ViewSerializer
    # authentication_classes = [JWTAuthentication]
    # authentication_classes = [BaseAuthentication]
    permission_classes = [IsAuthenticated]
