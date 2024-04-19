from django.contrib import admin
from django.contrib.admin import register
from django.utils.html import format_html

from .models import Episode, EpisodeOtherAuthor


# Register your models here.
@register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    # def image_tag(self, obj):
    #     return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))
    list_display = ('id', 'image_source', 'title', 'channel', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('title',)
    list_editable = ('is_active',)
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'channel__title')


@register(EpisodeOtherAuthor)
class EpisodeOtherAuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'episode', 'author', 'created_at', 'updated_at')
    list_display_links = ('episode', 'author')
    list_filter = ('episode', 'author', 'created_at', 'updated_at')
    search_fields = ('episode__title', 'author__username')
