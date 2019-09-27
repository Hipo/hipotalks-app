# Generated by Django 2.2.4 on 2019-09-26 09:23

from django.conf import settings
from django.db import migrations, models
import hipo_django_core.models
import hipo_django_core.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigIntegerField(default=hipo_django_core.utils.generate_unique_id, editable=False, primary_key=True, serialize=False)),
                ('creation_datetime', models.DateTimeField(auto_now_add=True)),
                ('update_datetime', models.DateTimeField(auto_now=True)),
                ('event_type', models.CharField(choices=[('hipotalks', 'Hipotalks'), ('townhall', 'Townhall')], max_length=255)),
                ('date', models.DateField()),
                ('is_completed', models.BooleanField(default=False)),
                ('canceled_users', models.ManyToManyField(related_name='canceled_events', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(related_name='events', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'ordering': ('-date',),
            },
            bases=(hipo_django_core.models.LogEntryMixin, models.Model),
        ),
    ]
