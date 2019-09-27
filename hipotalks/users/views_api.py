from rest_framework.generics import ListAPIView

from hipotalks.users.models import User
from hipotalks.users.serializers import BaseUserSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = BaseUserSerializer