from django.shortcuts import render, redirect
from createEvent.models import Event
from django.http import HttpResponse
from createEvent.forms import EventForm
from formofevent.forms import  EditForm


def show_form_of_event(request, pk):
    event = Event.objects.get(id=pk)
    context = {'event': event}
    return render(request, 'formofevent/form_of_event.html', context)


def party(request, pk):
    event = Event.objects.get(id=pk)
    user = request.user
    event.members_list.add(user)
    return redirect('map')


def leave_party(request, pk):
    event = Event.objects.get(id=pk)
    user = request.user
    event.members_list.remove(user)
    return redirect('map')


def edit_party(request, pk):
    event = Event.objects.get(id=pk)
    form = EditForm(instance=event)
    if request.method == 'POST':
        form = EditForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('map')
    data = {'form': form}

    return render(request, 'createevent/create.html', data)
