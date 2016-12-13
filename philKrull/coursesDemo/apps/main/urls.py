from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses$', views.add_course),
    url(r'^courses/destroy/(?P<course_id>\d*)$', views.destroy),
    url(r'^courses/delete/(?P<course_id>\d*)$', views.delete),
]
