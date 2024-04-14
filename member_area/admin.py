from django.contrib import admin
from django.contrib.admin import register

from .models import User, Channel, ChannelLink


# Register your models here.
@register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_source', 'username', 'gender', 'age', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('username', )
    list_editable = ('is_active',)
    list_filter = ('gender', 'is_active', 'created_at', 'updated_at')
    search_fields = ('username', 'age')


@register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_source', 'title', 'author', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('title',)
    list_editable = ('is_active',)
    list_filter = ('title', 'author', 'is_active', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'author__username')


@register(ChannelLink)
class ChannelLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'channel', 'link', 'created_at', 'updated_at')
    list_display_links = ('channel',)
    list_filter = ('channel', 'created_at', 'updated_at')
    search_fields = ('channel__title', 'link')

