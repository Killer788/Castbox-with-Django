from django.db import models
from django.forms import CharField

from member_area.models import User, Channel
from content.models import Episode


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated At'
    )

    class Meta:
        abstract = True

    def __str__(self):
        raise NotImplementedError('Please implement __str__ method.')


class UserSubscribe(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='user_subscribes',
        null=False,
        blank=False,
        verbose_name='User'
    )
    is_subscribed = models.BooleanField(
        default=True,
        verbose_name='Is Subscribed'
    )
    channel = models.ForeignKey(
        Channel,
        on_delete=models.PROTECT,
        related_name='user_subscribes',
        null=False,
        blank=False,
        verbose_name='Channel'
    )

    class Meta:
        verbose_name = 'User Subscribe'
        verbose_name_plural = 'User Subscribes'
        ordering = ('pk',)

    def __str__(self):
        return f'{self.user.username} subscription to {self.channel.title}'


class Comment(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='comments',
        null=False,
        blank=False,
        verbose_name='User'
    )
    text = models.TextField(null=False, blank=False, verbose_name='Text')
    episode = models.ForeignKey(
        Episode,
        on_delete=models.PROTECT,
        related_name='comments',
        null=False,
        blank=False,
        verbose_name='Episode'
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name='Is Active'
    )

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('pk',)

    def __str__(self):
        return self.text


class Like(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='likes',
        null=False,
        blank=False,
        verbose_name='User'
    )
    is_liked = models.BooleanField(
        default=True,
        verbose_name='Is Liked'
    )
    episode = models.ForeignKey(
        Episode,
        on_delete=models.PROTECT,
        related_name='likes',
        null=False,
        blank=False,
        verbose_name='Episode'
    )

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
        ordering = ('pk',)

    def __str__(self):
        return f'{self.user.username} liked {self.episode.title}'


class Playlist(BaseModel):
    title = CharField(max_length=250, null=False, blank=False, verbose_name='Title')
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='playlists',
        null=False,
        blank=False,
        verbose_name='User'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Is active'
    )

    class Meta:
        verbose_name = 'Playlist'
        verbose_name_plural = 'Playlists'
        ordering = ('pk',)

    def __str__(self):
        return self.title


class PlaylistEpisode(BaseModel):
    playlist = models.ForeignKey(
        Playlist,
        on_delete=models.PROTECT,
        related_name='playlist_episodes',
        null=False,
        blank=False,
        verbose_name='Playlist'
    )
    episode = models.ForeignKey(
        Episode,
        on_delete=models.PROTECT,
        related_name='playlist_episodes',
        null=False,
        blank=False,
        verbose_name='Episode'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Is Active'
    )

    class Meta:
        verbose_name = 'Playlist Episode'
        verbose_name_plural = 'Playlist Episodes'
        ordering = ('pk',)

    def __str__(self):
        return f'{self.playlist.title}{self.episode.title}'
