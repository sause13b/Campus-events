from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_data(request):
    if request.method == "POST":
        print(request.POST)
        return HttpResponse('ok', status=200)


def create_event(request):
    return render(request, 'createEvent/create_event.html')

