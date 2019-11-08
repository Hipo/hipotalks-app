from rest_framework import serializers

from hipotalks.events.models import Event
from hipotalks.slots.serializers import SlotSerializer


class EventSerializer(serializers.ModelSerializer):
    slots = SlotSerializer(many=True)

    class Meta:
        model = Event
        fields = (
            'id',
            'event_type',
            'date',
            'slots',
        )