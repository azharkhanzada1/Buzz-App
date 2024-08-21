from rest_framework import serializers
from .models import Post, Comment, Like, View

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'content', 'author', 'created_at']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'post', 'user', 'created_at']

class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = ['id', 'post', 'user', 'created_at']
