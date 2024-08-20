from django.contrib import admin
from .models import Post, Comment, Like, View

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author', 'created_at', 'updated_at']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'content', 'author', 'created_at']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['post', 'user', 'created_at']

@admin.register(View)
class ViewAdmin(admin.ModelAdmin):
    list_display = ['post', 'user', 'created_at']


