from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.user.is_authenticated:
        return redirect('map')
    else:
        form = RegisterForm()
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/login')

        return render(request, 'registration/register.html', {'form': form})


def login_page(request):
    if request.user.is_authenticated:
        return redirect('map')
    else:
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
