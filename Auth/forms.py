from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'user-login',
        'placeholder': 'Введите вашу почту'}))

    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={
        'class': 'pass-login',
        'placeholder': 'Введите пароль'}))


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'passw-reg',
        'placeholder': 'Придумайте пароль'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'passw-reg',
        'placeholder': 'Повторите пароль'
    }))

    class Meta:
        model = MyUser
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'user-reg',
                'placeholder': 'Введите имя',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'email-reg',
                'placeholder': 'Введите почту'

            })
        }
