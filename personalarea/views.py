from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm
from .forms import *
from datetime import date


def edit_profile(request):
    extended_user = request.user.extendeduser
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        form_ = EditProfileForm_(request.POST, request.FILES, instance=request.user.extendeduser)
        if form.is_valid() and form_.is_valid():
            form_.save()
            form.save()
            return redirect('show_personalarea')

    form = EditProfileForm(instance=request.user)
    form_ = EditProfileForm_(instance=request.user.extendeduser)
    args = {'form': form, 'form_': form_, 'user_': extended_user}
    return render(request, 'personalarea/edit_profile.html', args)


def show_personalarea(request):
    user_phone = request.user.extendeduser.phone
    extended_user = request.user.extendeduser
    context = {'phone': user_phone, 'user_': extended_user}
    return render(request, 'personalarea/index.html', context)


def planed_events(request):
    user = request.user
    today = date.today()
    u_events = user.members_set.all().filter(date__gte=today).order_by('date')
    context = {'user_events': u_events}
    return render(request, 'personalarea/planed_events.html', context)


def ended_events(request):
    user = request.user
    today = date.today()
    u_events = user.members_set.all().filter(date__lte=today).order_by('date')
    context = {'user_events': u_events}
    return render(request, 'personalarea/ended_events.html', context)


def planed_events(request):
    user = request.user
    today = date.today()
    u_events = user.members_set.all().filter(date__gte=today).order_by('date')
    context = {'user_events': u_events}
    return render(request, 'personalarea/planed_events.html', context)


def my_events(request):
    user = request.user
    u_events = user.author_set.all()
    print(u_events)
    context = {'user_events': u_events}
    return render(request, 'personalarea/my_events.html', context)





