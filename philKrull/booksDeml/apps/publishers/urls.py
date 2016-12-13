from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.create_publisher, name = 'create_publisher'),
    url(r'^add_book_to_publisher$', views.add_book_to_publisher, name = 'add_book_to_publisher')
]
