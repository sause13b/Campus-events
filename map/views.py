from django.shortcuts import render


def render_map(request):
    return render(request, 'map/index.html')
