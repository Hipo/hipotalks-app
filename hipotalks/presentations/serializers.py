from rest_framework import serializers

from hipotalks.presentations.models import Presentation


class PresentationSerializer(serializers.ModelSerializer):
    from hipotalks.users.serializers import BaseUserSerializer
    user = BaseUserSerializer()

    class Meta:
        model = Presentation
        fields = (
            'id',
            'title',
            'slide_link',
            'video_link',
            'user',
        )