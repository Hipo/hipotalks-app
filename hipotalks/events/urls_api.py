from django.conf.urls import url

from hipotalks.events.views_api import EventListAPIView

urlpatterns = [
        url(r'^$', EventListAPIView.as_view(), name='event-list'),
]