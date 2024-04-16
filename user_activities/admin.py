from django.contrib import admin
from django.contrib.admin import register

from .models import UserSubscribe, Comment, Like, Playlist, PlaylistEpisode


# Register your models here.
@register(UserSubscribe)
class UserSubscribeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'is_subscribed', 'channel', 'created_at', 'updated_at')
    list_display_links = ('user',)
    list_editable = ('is_subscribed',)
    list_filter = ('user', 'is_subscribed', 'channel', 'created_at', 'updated_at')
    search_fields = ('user__name', 'channel__title')


@register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'episode', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('user',)
    list_editable = ('is_active',)
    list_filter = ('user', 'episode', 'is_active', 'created_at', 'updated_at')
    search_fields = ('user__name', 'episode__title')


@register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'is_liked', 'episode', 'created_at', 'updated_at')
    list_display_links = ('user',)
    list_editable = ('is_liked',)
    list_filter = ('user', 'is_liked', 'episode', 'created_at', 'updated_at')
    search_fields = ('user__name', 'episode__title')


@register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('title',)
    list_editable = ('is_active',)
    list_filter = ('user', 'is_active', 'created_at', 'updated_at')
    search_fields = ('title', 'user__name')


@register(PlaylistEpisode)
class PlaylistEpisodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'playlist', 'episode', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('playlist',)
    list_editable = ('is_active',)
    list_filter = ('playlist', 'is_active', 'created_at', 'updated_at')
    search_fields = ('playlist__title', 'episode__title')
