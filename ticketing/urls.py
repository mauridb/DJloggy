from django.conf.urls import url

from ticketing import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
