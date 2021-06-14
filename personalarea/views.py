from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm
from .forms import EditProfileForm

def edit_profile(request):
    if request.method == 'POST':
        print(request.method == 'POST')
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('show_personalarea')

    form = EditProfileForm(instance=request.user)
    args = {'form': form}
    return render(request, 'personalarea/edit_profile.html', args)

def show_personalarea(request):
    return render(request, 'personalarea/index.html')





