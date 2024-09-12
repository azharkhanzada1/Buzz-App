from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Follow
from .serializers import FollowSerializer
from rest_framework.permissions import IsAuthenticated

class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        follower = request.user
        following_id = request.data.get('following')
        if follower.id == following_id:
            return Response({'error': "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)
        follow, created = Follow.objects.get_or_create(follower=follower, following_id=following_id)
        if created:
            return Response({'message': "Follow successfully!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'You are already following this user'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        follower = request.user
        following_id = kwargs.get('pk')
        follow = Follow.objects.filter(follower=follower, following_id=following_id).first()
        if follow:
            follow.delete()
            return Response({'message': "Unfollowed Successfully"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'You are not following this user.'}, status=status.HTTP_400_BAD_REQUEST)
