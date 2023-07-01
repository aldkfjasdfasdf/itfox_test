from django.contrib import admin

from .models import News, Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "username", "date")


@admin.register(Comment)
class CommenAdmin(admin.ModelAdmin):
    list_display = ("username", "text", "date")
