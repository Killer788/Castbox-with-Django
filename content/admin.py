from django.contrib import admin
from django.contrib.admin import register
from django.utils.html import format_html

from .models import Episode


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
