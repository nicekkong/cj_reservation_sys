from django.conf.urls import url

from .views import ConferenceDAV, ConferenceView

app_name = 'reservation'

urlpatterns = [
    url(r'^status/(?P<yyyymmdd>\d{8})/$', ConferenceView.as_view()),
    url(r'^status/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', ConferenceDAV.as_view()),
]