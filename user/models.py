from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username

    # class Meta:
    #     verbose_name = "user"
    #     verbose_name_plural = 'Users'
    #     ordering = ["username"]