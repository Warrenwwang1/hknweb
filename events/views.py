from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from .models import Event

def index(request):
    return redirect('calendar')


def calendar(request):
    events = Event.objects.order_by('-created_at')[:10]
    output = '\n'.join([str(event) for event in events])

    template = loader.get_template('events/calendar.html')
    context = {
        'events': output,
    }
    return HttpResponse(template.render(context, request))


def future(request):
    return HttpResponse("Hello, world. You're at the future index.")


def past(request):
    return HttpResponse("Hello, world. You're at the past index.")


def rsvps(request):
    return HttpResponse("Hello, world. You're at the rsvps index.")
