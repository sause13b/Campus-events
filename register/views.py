from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def registr(request):
    data = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            data['form'] = form
            data['res'] = "Всё прошло успешно"
            return render(request, 'register/registr.html', data)
    else:
        form = UserCreationForm()
        data['form'] = form
        # Рендаринг страницы
        return render(request, 'register/registr.html', data)