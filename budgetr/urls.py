from django.conf.urls import url, include
import views


urlpatterns = [
    url(r'^index/', views.index),
    url(r'^flows/', views.getflows),
    url(r'^newflow/', views.new_flow),
]

