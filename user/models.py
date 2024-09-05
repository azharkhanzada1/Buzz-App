from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password=None, **extra_fields ):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = None
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
