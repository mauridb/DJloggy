# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
from django.db import models
from django.contrib.auth.models import User

from loggy.settings import PROJECT_STATUS, TICKET_PRIORITY, TICKET_STATUS, TICKET_DIFFICULTY

logging.basicConfig(filename="platform.log", level=logging.DEBUG)


class Project(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=500)
    project_status = models.CharField(max_length=20, choices=PROJECT_STATUS)  # [started, in progress, closed]
    topic = models.CharField(max_length=100)
    deployed = models.BooleanField(default=False)
    project_effort = models.IntegerField(null=True, blank=True)  # estimated in days
    public_domain = models.URLField(null=True)
    started_at = models.DateTimeField(auto_now=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    deadline = models.DateField()

    def __str__(self):
        return "#{}-{}".format(self.id, self.title)


class Ticket(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=500)
    assigned_to = models.ForeignKey(User)
    ready = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=TICKET_PRIORITY)  # [high, normal, low]
    ticket_status = models.CharField(max_length=10, choices=TICKET_STATUS,
                                     default='Created')  # [tested, completed, in progress, created, cancelled]
    difficulty = models.CharField(max_length=10,
                                  choices=TICKET_DIFFICULTY)  # [very hard, hard, standard, simple, very simple]
    ticket_effort = models.DecimalField(max_digits=3, decimal_places=1)
    opened_at = models.DateTimeField(auto_now=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    delivery = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return "#{}-{}".format(self.id, self.title)
