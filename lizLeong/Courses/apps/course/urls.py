from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_course$', views.add),
    url(r'^remove_course/(?P<id>\d+)$', views.check),
    url(r'^remove/(?P<id>\d+)$', views.remove),
]

# '^ninjas/(?P<color>[a-zA-Z]+)
