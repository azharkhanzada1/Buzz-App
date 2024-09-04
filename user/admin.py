from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Display these fields in the admin list view
    list_display = ('email', 'username', 'phone_number', 'is_staff')

    # Add any fields you need in the admin form view
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number',)}),
    )