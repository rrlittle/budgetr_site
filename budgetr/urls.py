from django.conf.urls import url
from views import index


urlpatterns = [
    url(r'^(?P<end_yr>[0-9]{4})/(?P<end_mo>[0-9]{2})/(?P<end_day>[0-9]{2})/',
        index)
]
