from rest_framework import serializers

from hipotalks.presentations.serializers import PresentationSerializer
from hipotalks.slots.models import Slot
from hipotalks.users.serializers import UserSerializer


class SlotSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    presentation = PresentationSerializer()

    class Meta:
        model = Slot
        fields = (
            'id',
            'user',
            'presentation',
            'status',
        )