from django.shortcuts import render
from django.http import HttpResponse


def show_form_of_event(request):
    return render(request, 'formofevent/form_of_event.html')

