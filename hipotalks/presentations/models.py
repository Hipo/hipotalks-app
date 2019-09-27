from django.db import models
from hipo_django_core.models import AbstractBaseModel

from hipotalks.events.models import Event
from hipotalks.users.models import User


class Presentation(AbstractBaseModel):
    """
    It keeps presentations.
    """
    user = models.ForeignKey(User, related_name='presentations', on_delete=models.PROTECT)
    event = models.ForeignKey(Event, related_name='presentations', on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    slide_link = models.URLField(max_length=255, blank=True, null=True)
    video_link = models.URLField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Presentation'
        verbose_name_plural = 'Presentations'
        ordering = ('creation_datetime', )

    def __str__(self):
        return f'{self.title} - {self.user}'
