from django.contrib import admin
from django.contrib.admin import register

from .models import WatchEpisode, CheckChannel


# Register your models here.
@register(WatchEpisode)
class WatchEpisodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'episode', 'created_at')
    list_display_links = ('user',)
    list_filter = ('user', 'episode', 'created_at')
    search_fields = ('user__name', 'episode__title')


@register(CheckChannel)
class CheckChannelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'channel', 'created_at')
    list_display_links = ('user',)
    list_filter = ('user', 'channel', 'created_at')
    search_fields = ('user__name', 'channel__title')
