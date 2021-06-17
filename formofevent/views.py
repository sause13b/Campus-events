from django.shortcuts import render, redirect
from createEvent.models import Event
from django.http import HttpResponse, HttpResponseRedirect
from createEvent.forms import EventForm
from formofevent.forms import EditForm


def show_form_of_event(request, pk):
    event = Event.objects.get(id=pk)
    members_count = event.members_list.count()
    event.members = int(event.members)
    context = {'event': event, 'count': members_count}

    return render(request, 'formofevent/form_of_event.html', context)


def party(request, pk):
    event = Event.objects.get(id=pk)
    user = request.user
    event.members_list.add(user)
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


def leave_party(request, pk):
    event = Event.objects.get(id=pk)
    user = request.user
    event.members_list.remove(user)
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


def edit_party(request, pk):
    event = Event.objects.get(id=pk)
    form = EditForm(instance=event)
    if request.method == 'POST':
        form = EditForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('map')
    data = {'form': form, 'pk': pk}

    return render(request, 'createevent/edit.html', data)
