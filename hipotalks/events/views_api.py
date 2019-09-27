from rest_framework.generics import ListAPIView

from hipotalks.events.models import Event
from hipotalks.events.serializers import EventSerializer


class EventListAPIView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer