from django.shortcuts import render
from django.http import HttpResponse

def show_personalarea(request):
    print('Кто-то зашел на главную!')
    return HttpResponse('Привет!')

