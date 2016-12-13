from django.conf.urls import url
from . import views

# def index(request):
#     print "I will be your future routes; HTTP requests will be captured by me"

urlpatterns = [
    url(r'^$', views.index),
]
