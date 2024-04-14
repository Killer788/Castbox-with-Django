from django.db import models

from lib.common_base_models import BaseModelWithUpdatedAt, BaseModelWithIsActive, BaseModelWithTitleAndDescription


# Create your models here.
class User(BaseModelWithIsActive):
    username = models.CharField(
        max_length=25,
        unique=True,
        null=False,
        blank=False,
        verbose_name='Username'
    )
    password = models.CharField(
        max_length=25,
        null=False,
        blank=False,
        verbose_name='Password'
    )
    gender = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        verbose_name='Gender'
    )
    age = models.IntegerField(
        null=False,
        blank=False,
        verbose_name='Age'
    )
    image_source = models.TextField(null=True, blank=True, verbose_name="Image Source")

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('pk',)

    def __str__(self):
        return self.username


class Channel(BaseModelWithTitleAndDescription):
    image_source = models.TextField(null=True, blank=True, verbose_name="Image Source")
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        related_name='channels',
        verbose_name="Author"
    )

    class Meta:
        verbose_name = 'Channel'
        verbose_name_plural = 'Channels'
        ordering = ('pk',)

    def __str__(self):
        return self.title


class ChannelLink(BaseModelWithUpdatedAt):
    channel = models.ForeignKey(
        Channel,
        on_delete=models.PROTECT,
        related_name='channel_links',
        null=False,
        blank=False,
        verbose_name='Channel'
    )
    link = models.TextField(null=False, blank=False, verbose_name="Link")

    class Meta:
        verbose_name = 'Channel Link'
        verbose_name_plural = 'Channel Links'
        ordering = ('pk',)

    def __str__(self):
        return self.link
