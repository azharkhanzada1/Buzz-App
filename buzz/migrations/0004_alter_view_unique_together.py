# Generated by Django 5.1 on 2024-08-21 21:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buzz', '0003_alter_like_unique_together'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='view',
            unique_together={('post', 'user')},
        ),
    ]
