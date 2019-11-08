from rest_framework import serializers

from hipotalks.events.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'event_type',
            'date'
        )