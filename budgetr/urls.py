import django
from django.conf.urls import url, include
# from django.conf.ursl.default import patterns
import views

js_info_dict = {
    'packages': ('recurrence', ),
}

urlpatterns = [
    url(r'^index/', views.index),
	url(r'^flow/(?P<flowid>[0-9])/(?P<end_yr>[0-9]{4})/(?P<end_mo>[0-9]{2})/(?P<end_day>[0-9]{2})/',
        views.flow),
	url(r'^wealth/(?P<end_yr>[0-9]{4})/(?P<end_mo>[0-9]{2})/(?P<end_day>[0-9]{2})/',
        views.wealth),

	# required by recurrence
    url(r'^jsi18n/$', django.views.i18n.javascript_catalog, js_info_dict),
]

