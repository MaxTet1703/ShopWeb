from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from .forms import *
from .models import *
from .mixin import *


# Create your views here.

class UserRegister(View):
    template_name = "register.html"

    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect(self.get_redirect_url())
        context = {
            'form': RegisterForm(),
            'title': 'Регистрация'
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegisterForm(request.POST)

        for em in list(MyUser.objects.all().values("email")):
            if em['email'] == self.request.POST.get('email'):
                return JsonResponse(data={
                    'status': 400,
                    'error': "Пользователь с такой почтйо уже существует"
                }, status=200)
        if self.request.POST.get('password1') != self.request.POST.get('password2'):
            return JsonResponse(data={
                'status': 400,
                'error': "Пароли не совпадают"
            }, status=200)
        if form.is_valid():
            form.save()
            email = self.request.POST.get('email')
            name = self.request.POST.get('name')
            password = self.request.POST.get('password1')
        else:
            return JsonResponse(data={
                'status': 400,
                'error': "Введите данные правильно",
            }, status=200)
        MyUser.objects.create(email=email, name=name, password=password, is_cook=False)
        return JsonResponse(data={
            'status': 200,
            'success': 'Вы успешно зарегистрировались',
        }, status=200)


class UserLogin(View, DataMixIn):
    template_name = 'login.html'

    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect(self.get_redirect_url())
        context = {
            'form': LoginForm(),
            'title': 'Регистрация'
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = LoginForm(request.POST)
        if not form.is_valid():
            return JsonResponse(data={
                'status': 400,
                'error': "Неверная почта или пароль",
            }, status=200)
        email = self.request.POST.get('email')
        password = self.request.POST.get("password")
        print(email)
        print(password)
        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect(self.get_redirect_url())
        return JsonResponse(data={
            'status': 400,
            'error': "Неверная почта или пароль",
        }, status=200)


def logout_user(request):
    logout(request)
    return redirect('login')
