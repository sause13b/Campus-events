from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Campus_events.decorators import *
from personalarea.models import *


@unauthenticated_user
def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            ExtendedUser.objects.create(user=user)
            return redirect('/login')

    return render(request, 'registration/register.html', {'form': form})

@unauthenticated_user
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('map')
        else:
            messages.info(request, 'Username or password in incorrect')

    return render(request, "registration/login.html")

def log_out(request):
    logout(request)
    return redirect('login')
