from django.db import models
from hipo_django_core.models import AbstractBaseModel

from hipotalks.events.models import Event
from hipotalks.users.models import User


class Blacklist(AbstractBaseModel):
    """
    It keeps users who skip their presentation.
    """
    user = models.ForeignKey(User, related_name='blacklist', on_delete=models.PROTECT)
    event = models.ForeignKey(Event, related_name='blacklist', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.user} - {self.event}"
