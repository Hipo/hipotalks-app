from __future__ import unicode_literals

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.utils.translation import ugettext_lazy as _
from hipo_django_core.models import AbstractBaseModel
from hipo_django_core.utils import generate_unique_id


class User(AbstractBaseModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name=_('Email'), unique=True, db_index=True)
    username = models.CharField(_('Username'), max_length=150, unique=True)
    first_name = models.CharField(_('First Name'), max_length=255)
    last_name = models.CharField(_('Last Name'), max_length=255, blank=True)
    date_joined = models.DateTimeField(_('Date Joined'), auto_now_add=True, editable=False)
    is_active = models.BooleanField(verbose_name=_('Active Status'), default=True)
    is_staff = models.BooleanField(verbose_name=_('Staff Status'), default=False)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name']

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ('first_name', 'last_name')

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.first_name