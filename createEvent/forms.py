from createEvent.models import Event
from django.forms import ModelForm, TextInput, Textarea


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['address', 'members', 'vk', 'email', 'phone', 'name', 'info']

        widgets = {
            "name": TextInput(attrs={
                "class": 'from-control',
                "placeholder": 'Название мероприятия'
            }),
            "members": TextInput(attrs={
                "class": 'from-control',
                "placeholder": 'Количество участников'
            }),
            "address": TextInput(attrs={
                "class": 'from-control',
                "placeholder": 'Адресс мероприятия'
            }),
            "vk": TextInput(attrs={
                "class": 'from-control',
                "placeholder": 'Вконтакте'
            }),
            "email": TextInput(attrs={
                "class": 'from-control',
                "placeholder": 'Почта'
            }),
            "phone": TextInput(attrs={
                "class": 'from-control',
                "placeholder": 'Телефон'
            }),
            "info": Textarea(attrs={
                "class": 'from-control',
                "placeholder": 'Информация о мероприятии'
            }),
        }