# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from ticketing.models import Ticket


# Register your models here.
from ticketing.models import Ticket, Project

admin.site.register(Project)
admin.site.register(Ticket)
