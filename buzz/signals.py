from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Like, Comment, View, Post

@receiver(post_save, sender=Like)
def handle_like_save(sender, instance, created, **kwargs):
    if created:
        instance.post.like_count += 1
        instance.post.save()

@receiver(post_delete, sender=Like)
def handle_like_delete(sender, instance, **kwargs):
    instance.post.like_count -= 1
    instance.post.save()

@receiver(post_save, sender=Comment)
def handle_comment_save(sender, instance, created, **kwargs):
    if created:
        instance.post.comment_count += 1
        instance.post.save()

@receiver(post_delete, sender=Comment)
def handle_comment_delete(sender, instance, **kwargs):
    instance.post.comment_count -= 1
    instance.post.save()

@receiver(post_save, sender=View)
def handle_view_save(sender, instance, created, **kwargs):
    if created:
        instance.post.view_count += 1
        instance.post.save()

@receiver(post_delete, sender=View)
def handle_view_delete(sender, instance, **kwargs):
    instance.post.view_count -= 1
    instance.post.save()