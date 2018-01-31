from django.conf.urls import url

from .views import *

app_name = 'reservation'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^status/today/$', TodayView.as_view(), name='today'),
    url(r'^status/(?P<yyyymmdd>\d{8})/(?P<test>[a-z]+)/$', ConferenceView.as_view(), name='status'),
    url(r'^status/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', ConferenceDAV.as_view()),
    url(r'^save/$', ConferenceSave.as_view(), name='status_save'),
]