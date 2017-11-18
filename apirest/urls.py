from django.conf.urls import url

from apirest import views

urlpatterns = [
    url(r'^v1/', views.api_root, name='api-root'),
]
