from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import Post, Comment, Like, View
from .serializers import PostSerializer, CommentSerializer, LikeSerializer, ViewSerializer
from .pagination import BuzzLimitOffsetPagination

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = BuzzLimitOffsetPagination
    filter_backends = [SearchFilter]
    search_fields = ['title']



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class ViewViewSet(viewsets.ModelViewSet):
    queryset = View.objects.all()
    serializer_class = ViewSerializer
