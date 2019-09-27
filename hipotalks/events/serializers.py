from rest_framework import serializers

from hipotalks.events.models import Event
from hipotalks.users.serializers import UserSerializer, BaseUserSerializer


class EventSerializer(serializers.ModelSerializer):
    from hipotalks.presentations.serializers import PresentationSerializer
    presentations = PresentationSerializer(many=True)
    canceled_users = BaseUserSerializer(many=True)

    class Meta:
        model = Event
        fields = (
            'id',
            'event_type',
            'date',
            'presentations',
            'canceled_users',
            'is_completed',
            'creation_datetime',
            'update_datetime',
        )