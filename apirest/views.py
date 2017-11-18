# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apirest.serializers import ProjectSerializer, TicketSerializer, UserSerializer
from ticketing.models import Project, Ticket
from django.contrib.auth.models import User


class ProjectViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    model = Project
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # filter_fields = ('title',)


class TicketViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                    mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    model = Ticket
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    # filter_fields = ('title',)


class UserViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # filter_fields = ('username',)
