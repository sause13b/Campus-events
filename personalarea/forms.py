from django import forms
from django.contrib.auth.models import AbstractUser, User
from .models import *
from django.contrib.auth.forms import UserChangeForm


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name'
        )
        widgets = {
            'email': forms.TextInput(attrs={'class': 'changing_form'}),
            'first_name': forms.TextInput(attrs={'class': 'changing_form'}),
            'last_name': forms.TextInput(attrs={'class': 'changing_form'}),
        }


class EditProfileForm_(forms.ModelForm):
    class Meta:
        model = ExtendedUser
        fields = '__all__'
        exclude = ['user']

        widgets = {
            'phone': forms.TextInput(attrs={'class': 'changing_form'}),
        }