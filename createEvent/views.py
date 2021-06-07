from django.shortcuts import render
from django.http import HttpResponse


def create_event(request):
    return render(request, 'createEvent/create_event.html')

