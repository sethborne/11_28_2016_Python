from django.conf.urls import url
from . import views
# from django.contrib import admin

def index(request):
    print('8'*100)

urlpatterns = [
    url(r'^$', views.index),
]
