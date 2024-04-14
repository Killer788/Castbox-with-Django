from django.db import models

from content.models import Episode
from member_area.models import User, Channel


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At'
    )

    class Meta:
        abstract = True

    def __str__(self):
        raise NotImplementedError('Please Implement __str__ method.')


class WatchEpisode(BaseModel):
    user = models.ForeignKey(
        User,
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
        User,
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
