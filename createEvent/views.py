from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from createEvent.forms import EventForm


@csrf_exempt
def get_data(request):
    if request.method == "POST":
        print(request.POST)
        return HttpResponse('ok', status=200)


def create(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('map')

    data = {
        'form': form,
    }

    return render(request, 'createevent/create.html', data)


def show_form(request):
    return render(request, 'createevent/create_event.html')

