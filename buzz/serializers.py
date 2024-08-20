from rest_framework import serializers
from .models import *

class PostSerializer(serializers.Serializer):
    class Meta:
        models = Post
        fields = ['id','title', 'content', 'author', 'created_at', 'updated_at']

class CommentSerializer(serializers.Serializer):
    class Meta:
        models = Comment
        fields = ['id','post', 'content', 'author', 'created_at']

class LikeSerializer(serializers.Serializer):
    class Meta:
        models = Like
        fields = ['id','post', 'user', 'created_at']

class ViewSerializer(serializers.Serializer):
    class Meta:
        models = View
        fields = ['id', 'post', 'user', 'created_at']