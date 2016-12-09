# 9 from project level url, you are here.
from django.conf.urls import url
# 10 include views(controller in a MVC structure)
from . import views
urlpatterns = [
# 11 send to approiate controller method
    url(r'^$', views.index),
]
