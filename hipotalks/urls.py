from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls import include


api_urlpatterns = [
    url(r'^api/events/', include('hipotalks.events.urls_api')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += api_urlpatterns