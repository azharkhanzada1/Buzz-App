from django.conf import settings
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from Backend.settings import CACHES, CACHE_TTL
from buzz.models import Post, Comment, Like, View
from .serializers import PostSerializer, CommentSerializer, LikeSerializer, ViewSerializer
from .pagination import BuzzLimitOffsetPagination
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = BuzzLimitOffsetPagination
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content', "author__email"]

    @method_decorator(cache_page(60 * 15))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

@method_decorator(cache_page(60 * 5), name='dispatch')
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class ViewViewSet(viewsets.ModelViewSet):
    queryset = View.objects.all()
    serializer_class = ViewSerializer
