from django.shortcuts import render, redirect
from createEvent.forms import EventForm


def show_form_of_event(request):
    return render(request, 'formofevent/form_of_event.html')
