from django.apps import AppConfig
from django.db.models.signals import post_save


class EventConfig(AppConfig):
    name = 'events'
