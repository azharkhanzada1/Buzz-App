from django.core.mail import send_mail
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from notification.models import Notification

from notification.views import NotificationView
# from jsonschema.benchmarks.unused_registry import instance

from .models import Like, Comment, View, Post
from django.core.cache import cache

@receiver(post_save, sender=Like)
def handle_like_save(sender, instance, created, **kwargs):
    if created:
        instance.post.like_count += 1
        instance.post.save()
        cache.clear()

@receiver(post_delete, sender=Like)
def handle_like_delete(sender, instance, **kwargs):
    instance.post.like_count -= 1
    instance.post.save()
    cache.clear()

@receiver(post_save, sender=Comment)
def handle_comment_save(sender, instance, created, **kwargs):
    if created:
        instance.post.comment_count += 1
        instance.post.save()
        cache.clear()

@receiver(post_delete, sender=Comment)
def handle_comment_delete(sender, instance, **kwargs):
    instance.post.comment_count -= 1
    instance.post.save()
    cache.clear()

@receiver(post_save, sender=View)
def handle_view_save(sender, instance, created, **kwargs):
    if created:
        instance.post.view_count += 1
        instance.post.save()
        cache.clear()

@receiver(post_delete, sender=View)
def handle_view_delete(sender, instance, **kwargs):
    instance.post.view_count -= 1
    instance.post.save()
    cache.clear()

@receiver(post_save, sender=Comment)
def notify_on_comment(sender, instance, created, **kwargs):
    if created:
        message = f"{instance.author.email} commented on your post."
        Notification.objects.create(user=instance.post.author, post=instance.post, message=message)

@receiver(post_save, sender=Like)
def notify_on_like(sender, instance, created, **kwargs):
    if created:
        message = f"{instance.user.email} liked your post."
        Notification.objects.create(user=instance.post.author, post=instance.post, message=message)