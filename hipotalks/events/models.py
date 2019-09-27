from django.db import models
from hipo_django_core.models import AbstractBaseModel

from hipotalks.users.models import User


class Event(AbstractBaseModel):
    """
    It holds events.
    """
    EVENT_TYPE_HIPOTALKS = 'hipotalks'
    EVENT_TYPE_TOWNHALL = 'townhall'
    EVENT_TYPE_CHOICES = (
        (EVENT_TYPE_HIPOTALKS, 'Hipotalks'),
        (EVENT_TYPE_TOWNHALL, 'Townhall')
    )

    users = models.ManyToManyField(User, related_name='events')
    canceled_users = models.ManyToManyField(User, related_name='canceled_events', blank=True, null=True)
    event_type = models.CharField(choices=EVENT_TYPE_CHOICES, max_length=255)
    date = models.DateField()
    is_completed = models.BooleanField(default=False)
    is_canceled = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ('-date', )

    def __str__(self):
        return f'{self.date}'