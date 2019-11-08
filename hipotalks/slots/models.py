from django.db import models
from django.utils.translation import ugettext_lazy as _

from hipo_django_core.models import AbstractBaseModel

from hipotalks.events.models import Event
from hipotalks.presentations.models import Presentation
from hipotalks.users.models import User


class Slot(AbstractBaseModel):
    """
    It keeps users and their status information for each event.
    """
    STATUS_DID_THE_PRESENTATION = 'did-the-presentation'
    STATUS_MUCBIR = 'mucbir'
    STATUS_FAIL = 'fail'
    STATUS_NONE = None

    STATUS_CHOICES = (
        (STATUS_DID_THE_PRESENTATION, _('Did the presentation')),
        (STATUS_MUCBIR, _('Mucbir')),
        (STATUS_FAIL, _('Fail')),
        (STATUS_NONE, _('None')),
    )

    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='slots')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='slots')
    presentation = models.ForeignKey(Presentation, on_delete=models.PROTECT, related_name='slot', blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, default=STATUS_NONE, blank=True, null=True, max_length=255)

    class Meta:
        verbose_name = _('Slot')
        verbose_name_plural = _('Slots')
        ordering = ('event__date',)

    def __str__(self):
        return f'{self.event.date} - {self.user.full_name}'
