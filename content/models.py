from django.db import models

from member_area.models import Channel
from lib.common_base_models import BaseModelWithTitleAndDescription


# Create your models here.
class Episode(BaseModelWithTitleAndDescription):
    # image = models.ImageField(upload_to='./Images/Episodes/', null=True, blank=True, verbose_name="Image")
    image_source = models.TextField(null=True, blank=True, verbose_name="Image Source")
    channel = models.ForeignKey(Channel, on_delete=models.PROTECT, related_name='episodes', verbose_name="Channel")
    play_link = models.TextField(null=False, blank=False, verbose_name="Play Link")

    class Meta:
        verbose_name = "Episode"
        verbose_name_plural = "Episodes"
        ordering = ('pk',)

    def __str__(self):
        return self.title
