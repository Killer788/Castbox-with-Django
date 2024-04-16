from django.db import models
from django.contrib.auth import get_user_model

from lib.common_base_models import BaseModelWithUpdatedAt, BaseModelWithIsActive, BaseModelWithTitleAndDescription


BaseUser = get_user_model()


# Create your models here.
class User(BaseModelWithIsActive):
    GENDER_CHOICES = (
        ('Hide', 'Hide'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    AGE_CHOICES = (
        ('Hide', 'Hide'),
        ('Before 1950', 'Before 1950'),
        ('1950 - 1959', '1950 - 1959'),
        ('1960 - 1969', '1960 - 1969'),
        ('1970 - 1979', '1970 - 1979'),
        ('1980 - 1989', '1980 - 1989'),
        ('1990 - 1999', '1990 - 1999'),
        ('After 2000', 'After 2000'),
    )

    user = models.ForeignKey(
        BaseUser,
        on_delete=models.PROTECT,
        related_name='users',
        null=False,
        blank=False,
        verbose_name='User'
    )
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        default='Hide',
        verbose_name='Gender'
    )
    age = models.CharField(
        max_length=20,
        choices=AGE_CHOICES,
        default='Hide',
        verbose_name='Age'
    )
    image_source = models.TextField(null=True, blank=True, verbose_name="Image Source")

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('pk',)

    def __str__(self):
        return self.user.username


class Channel(BaseModelWithTitleAndDescription):
    image_source = models.TextField(null=True, blank=True, verbose_name="Image Source")
    author = models.ForeignKey(
        BaseUser,
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
    SOCIAL_MEDIA_CHOICES = (
        ('Instagram', 'Instagram'),
        ('Twitter', 'Twitter'),
        ('Telegram', 'Telegram'),
        ('Discord', 'Discord'),
        ('Youtube', 'Youtube'),
    )
    channel = models.ForeignKey(
        Channel,
        on_delete=models.PROTECT,
        related_name='channel_links',
        null=False,
        blank=False,
        verbose_name='Channel'
    )
    social_media = models.CharField(
        max_length=10,
        choices=SOCIAL_MEDIA_CHOICES,
        default='Instagram',
        verbose_name="Social Media"
    )
    link = models.TextField(null=False, blank=False, verbose_name="Link")

    class Meta:
        verbose_name = 'Channel Link'
        verbose_name_plural = 'Channel Links'
        ordering = ('pk',)

    def __str__(self):
        return self.link
