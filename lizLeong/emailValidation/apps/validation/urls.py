from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^validate$', views.validate), ##May need some id to access to db here???
    url(r'^success$', views.success),
]
