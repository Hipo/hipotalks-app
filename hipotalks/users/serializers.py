from rest_framework import serializers

from hipotalks.users.models import User


class BaseUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'is_active',
        )


class UserSerializer(BaseUserSerializer):
    from hipotalks.presentations.serializers import PresentationSerializer
    presentations = PresentationSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'presentations',
        )
