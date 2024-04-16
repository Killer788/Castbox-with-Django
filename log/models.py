from django.db import models

from content.models import Episode
from member_area.models import BaseUser, Channel
from lib.common_base_models import BaseModel


# Create your models here.
class WatchEpisode(BaseModel):
    user = models.ForeignKey(
        BaseUser,
        on_delete=models.PROTECT,
        related_name='watch_episodes',
        null=False,
        blank=False,
        verbose_name='User'
    )
    episode = models.ForeignKey(
        Episode,
        on_delete=models.PROTECT,
        related_name='watch_episodes',
        null=False,
        blank=False,
        verbose_name='Episode'
    )

    class Meta:
        verbose_name = 'Watch Episode'
        verbose_name_plural = 'Watch Episodes'
        ordering = ('pk',)

    def __str__(self):
        return f'{self.user.username} watched {self.episode.title}'


class CheckChannel(BaseModel):
    user = models.ForeignKey(
        BaseUser,
        on_delete=models.PROTECT,
        related_name='check_channels',
        null=False,
        blank=False,
        verbose_name='User'
    )
    channel = models.ForeignKey(
        Channel,
        on_delete=models.PROTECT,
        related_name='check_channels',
        null=False,
        blank=False,
        verbose_name='Channel'
    )

    class Meta:
        verbose_name = 'Check Channel'
        verbose_name_plural = 'Check Channels'
        ordering = ('pk',)

    def __str__(self):
        return f'{self.user.username} checked {self.channel.title}'
