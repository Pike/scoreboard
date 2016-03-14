from django.conf.urls import include, url

from . import views
import mqm_base.urls

urlpatterns = [
    url('^$', views.index),
    url('^', include(mqm_base.urls))
]
