from rest_framework.generics import ListAPIView

from hipotalks.events.models import Event
from hipotalks.events.serializers import EventSerializer


class EventListAPIView(ListAPIView):
    queryset = Event.objects.order_by('date')
    serializer_class = EventSerializer