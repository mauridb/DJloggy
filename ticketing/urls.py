from django.conf.urls import url

from ticketing import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
]
