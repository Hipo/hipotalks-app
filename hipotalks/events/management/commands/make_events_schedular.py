from django.core.management.base import BaseCommand
from django.conf import settings

from hipotalks.users.utils import create_scheduler


class Command(BaseCommand):
    """
    This command makes scheduler and creates events.
    """
    def handle(self, *args, **options):
        while True:
            create_scheduler()