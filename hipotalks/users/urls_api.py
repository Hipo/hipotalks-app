from django.conf.urls import url

from hipotalks.users.views_api import UserListAPIView

urlpatterns = [
        url(r'^$', UserListAPIView.as_view(), name='user-list'),
]