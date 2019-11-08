from django.db import models
from hipo_django_core.models import AbstractBaseModel
from django.utils.translation import ugettext_lazy as _


class Presentation(AbstractBaseModel):
    """
    It keeps presentations.
    """
    title = models.CharField(_('Title'), max_length=255)
    slide_link = models.CharField(_('Slide Link'), max_length=255)
    video_link = models.CharField(_('Video Link'), max_length=255, blank=True)

    class Meta:
        verbose_name = _('Presentation')
        verbose_name_plural = _('Presentations')