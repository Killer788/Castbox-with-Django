from django.contrib import admin
from django.contrib.admin import register

from .models import User, Channel, ChannelLink


# Register your models here.
@register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_source', 'user', 'gender', 'age', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('user', )
    list_editable = ('is_active',)
    list_filter = ('gender', 'is_active', 'created_at', 'updated_at')
    search_fields = ('user__name', 'age')


@register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_source', 'title', 'author', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('title',)
    list_editable = ('is_active',)
    list_filter = ('title', 'author', 'is_active', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'author__user__name')


@register(ChannelLink)
class ChannelLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'channel', 'social_media', 'link', 'created_at', 'updated_at')
    list_display_links = ('channel',)
    list_filter = ('channel', 'social_media', 'created_at', 'updated_at')
    search_fields = ('channel__title', 'social_media', 'link')

