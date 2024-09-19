from django.conf import settings
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from Backend.settings import CACHES, CACHE_TTL
from buzz.models import Post, Comment, Like, View
from .serializers import PostSerializer, CommentSerializer, LikeSerializer, ViewSerializer
from .pagination import BuzzLimitOffsetPagination
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from follow.models import Follow
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.views import APIView
from buzz.utils import fetch_data_from_api


# Follow ViewSet
class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        followed_users = Follow.objects.filter(follower=user).values_list('following_id', flat=True)
        return Post.objects.filter(author_id__in=followed_users)

# Post ViewSet (with caching and rate limiting)
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = BuzzLimitOffsetPagination
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content', "author__email"]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]  # Apply rate limiting here

    @method_decorator(cache_page(60 * 15))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

# Comment ViewSet with caching
@method_decorator(cache_page(60 * 5), name='dispatch')
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# Like ViewSet
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

# View ViewSet
class ViewViewSet(viewsets.ModelViewSet):
    queryset = View.objects.all()
    serializer_class = ViewSerializer

# External API Data View
class ExternalAPIDataView(APIView):
    def get(self, request, *args, **kwargs):
        # Replace the URL with the correct endpoint or fix the URL issue
        # data = fetch_data_from_api("http://127.0.0.1:8000/external-data/")  # Make sure this URL exists
        # return Response(data)
        return Response({"message": "Test API is working!"})