from django.shortcuts import render
from django.http import HttpResponse


def show_personalarea(request):
    return render(request, 'personalarea/index.html')



