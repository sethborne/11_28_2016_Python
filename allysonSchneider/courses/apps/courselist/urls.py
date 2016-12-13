from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addcourse$', views.addcourse),
    url(r'^destroy/(?P<id>\d+)', views.confirm),
    url(r'^confirm/(?P<id>\d+)', views.destroy)
]
