# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from ticketing.models import Project, Ticket


def index(request):
    return render(request, 'index.html')


def dashboard(request):
    projects = Project.objects.all()
    tickets = Ticket.objects.all()
    context = {
        'projects': projects,
        'tickets': tickets
    }
    return render(request, 'dashboard.html', context=context)


