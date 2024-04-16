from django.db import models

from member_area.models import BaseUser, Channel
from content.models import Episode
from lib.common_base_models import BaseModelWithUpdatedAt, BaseModelWithIsActive


# Create your models here.
class UserSubscribe(BaseModelWithUpdatedAt):
    user = models.ForeignKey(
        BaseUser,
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
        return f'{self.user.name} subscription to {self.channel.title}'


class Comment(BaseModelWithUpdatedAt):
    user = models.ForeignKey(
        BaseUser,
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


class Like(BaseModelWithUpdatedAt):
    user = models.ForeignKey(
        BaseUser,
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
        return f'{self.user.name} liked {self.episode.title}'


class Playlist(BaseModelWithIsActive):
    title = models.CharField(max_length=250, null=False, blank=False, verbose_name='Title')
    user = models.ForeignKey(
        BaseUser,
        on_delete=models.PROTECT,
        related_name='playlists',
        null=False,
        blank=False,
        verbose_name='User'
    )

    class Meta:
        verbose_name = 'Playlist'
        verbose_name_plural = 'Playlists'
        ordering = ('pk',)

    def __str__(self):
        return self.title


class PlaylistEpisode(BaseModelWithIsActive):
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

    class Meta:
        verbose_name = 'Playlist Episode'
        verbose_name_plural = 'Playlist Episodes'
        ordering = ('pk',)

    def __str__(self):
        return f'{self.playlist.title}{self.episode.title}'
