from django.conf.urls import url, include

from apirest import views
from rest_framework.routers import  DefaultRouter
from apirest.views import ProjectViewSet, TicketViewSet, UserViewSet

router_v1 = DefaultRouter()

router_v1.register(r'projects', ProjectViewSet)
router_v1.register(r'tickets', TicketViewSet)
router_v1.register(r'users', UserViewSet)


urlpatterns = [

    url(r'^v1/', include(router_v1.urls, namespace='api-root')),
]
