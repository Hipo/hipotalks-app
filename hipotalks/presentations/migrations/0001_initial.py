# Generated by Django 2.2.4 on 2019-11-01 14:56

from django.db import migrations, models
import hipo_django_core.models
import hipo_django_core.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.BigIntegerField(default=hipo_django_core.utils.generate_unique_id, editable=False, primary_key=True, serialize=False)),
                ('creation_datetime', models.DateTimeField(auto_now_add=True)),
                ('update_datetime', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slide_link', models.CharField(max_length=255, verbose_name='Slide Link')),
                ('video_link', models.CharField(blank=True, max_length=255, verbose_name='Video Link')),
            ],
            options={
                'verbose_name': 'Presentation',
                'verbose_name_plural': 'Presentations',
            },
            bases=(hipo_django_core.models.LogEntryMixin, models.Model),
        ),
    ]
