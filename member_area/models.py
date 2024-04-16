from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from lib.common_base_models import BaseModelWithUpdatedAt, BaseModelWithIsActive, BaseModelWithTitleAndDescription


# Create your models here.
class CustomAccountManager(BaseUserManager):
    def create_user(self, username, password, **other_fields):
        user = self.model(username=username, password=password, **other_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')

        return self.create_user(username, password, **other_fields)


class User(BaseModelWithIsActive, AbstractBaseUser, PermissionsMixin):
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

    username = models.CharField(
        max_length=25,
        unique=True,
        null=False,
        blank=False,
        verbose_name='Username'
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
    is_staff = models.BooleanField(default=False, verbose_name="Is Staff")

    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'

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
