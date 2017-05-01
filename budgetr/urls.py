from django.conf.urls import url
import views


urlpatterns = [
    url(r'^(?P<end_yr>[0-9]{4})/(?P<end_mo>[0-9]{2})/(?P<end_day>[0-9]{2})/',
        views.index),
	url(r'^flow/(?P<flowid>[0-9])/(?P<end_yr>[0-9]{4})/(?P<end_mo>[0-9]{2})/(?P<end_day>[0-9]{2})/',
        views.flow),
	url(r'^wealth/(?P<end_yr>[0-9]{4})/(?P<end_mo>[0-9]{2})/(?P<end_day>[0-9]{2})/',
        views.wealth),
    
]
