from django.contrib import admin
from follow.models import Follow
# Register your models here.

class FollowAdmin(admin.ModelAdmin):
    list_display = ('follower', 'following', 'created_at')
    search_fields = ('follower__email', 'following__email')
    list_filter = ('created_at',)

admin.site.register(Follow, FollowAdmin)