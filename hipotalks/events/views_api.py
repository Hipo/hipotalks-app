from rest_framework.generics import ListAPIView

from hipotalks.events.models import Event
from hipotalks.events.serializers import EventSerializer


class EventListAPIView(ListAPIView):
    queryset = Event.objects.filter(is_canceled=False).order_by('date')
    serializer_class = EventSerializer