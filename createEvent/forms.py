from createEvent.models import Event
from django.forms import ModelForm, TextInput, Textarea, CheckboxSelectMultiple
from django import forms


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['address', 'members', 'vk', 'email', 'phone', 'name', 'info', 'lat', 'lng', 'date', 'tags']

        widgets = {
            "name": TextInput(attrs={
                "class": 'from-control',
            }),
            "members": TextInput(attrs={
                "class": 'from-control',
            }),
            "address": TextInput(attrs={
                "class": 'from-control',
            }),
            "vk": TextInput(attrs={
                "class": 'from-control',
            }),
            "email": TextInput(attrs={
                "class": 'from-control',
            }),
            "phone": TextInput(attrs={
                "class": 'from-control',
            }),
            "info": Textarea(attrs={
                "class": 'from-control',
                "placeholder": 'Информация о мероприятии'
            }),
            "lat": TextInput(attrs={
                "class": 'hidden',
            }),
            "lng": TextInput(attrs={
                "class": 'hidden',
            }),
            "tags": CheckboxSelectMultiple()
        }

    def clean(self):
        cleaned_data = super(EventForm, self).clean()
        errors = []
        if Event.objects.filter(name=cleaned_data['name']).exists():
            errors.append(forms.ValidationError("Эвент с таким названием уже существует"))
        if not (cleaned_data['phone'] or cleaned_data['email'] or cleaned_data['vk']):
            errors.append(forms.ValidationError("Должен быть указан хотя бы 1 способ связи"))
        if not cleaned_data['date']:
            errors.append(forms.ValidationError("Дата проведения не указана"))
        if not cleaned_data['lat']:
            errors.append(forms.ValidationError("Укажите место проведения на карте"))
        if errors:
            raise forms.ValidationError(errors)
        return self.cleaned_data
