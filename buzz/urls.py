from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from buzz.views import PostViewSet, CommentViewSet, LikeViewSet, ViewViewSet, ExternalAPIDataView
from buzz.consumers import PostConsumer

urlpatterns = [

]
# DefaultRouter for API endpoints
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'views', ViewViewSet)

# URL patterns for API and external data view
urlpatterns = [
    path('', include(router.urls)),  # API routes
    path('external-data/', ExternalAPIDataView.as_view(), name='external_data'),  # External API data view
]

# WebSocket URL patterns for real-time post updates
websocket_urlpatterns = [
    re_path(r'ws/posts/$', PostConsumer.as_asgi()),  # WebSocket endpoint for posts
]
