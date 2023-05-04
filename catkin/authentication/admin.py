from .models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['email', 'is_active']
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        ('Personal info', {
            'fields': ('username', 'is_active')
        }),
        ('Permissions', {
            'fields': (
                'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password1', 'password2')
        }),
    )

    list_per_page = 25
