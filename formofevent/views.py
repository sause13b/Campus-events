from django.shortcuts import render, redirect
from createEvent.models import Event


def show_form_of_event(request, pk):
    event = Event.objects.get(id=pk)
    context = {'event': event}
    return render(request, 'formofevent/form_of_event.html', context)
