from django.db import models

from member_area.models import Channel


# Create your models here.
class Episode(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False, verbose_name="Title")
    description = models.TextField(null=False, blank=False, verbose_name="Description")
    # image = models.ImageField(upload_to='./Images/Episodes/', null=True, blank=True, verbose_name="Image")
    image_source = models.TextField(null=True, blank=True, verbose_name="Image Source")
    channel = models.ForeignKey(Channel, on_delete=models.PROTECT, related_name='episodes', verbose_name="Channel")
    play_link = models.TextField(null=False, blank=False, verbose_name="Play Link")
    is_active = models.BooleanField(default=False, verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Episode"
        verbose_name_plural = "Episodes"
        ordering = ('pk',)

    def __str__(self):
        return self.title
