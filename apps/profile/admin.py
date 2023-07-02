from django.contrib import admin

from apps.profile.models import User, Token


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "role")
