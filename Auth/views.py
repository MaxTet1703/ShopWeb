from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView

from .forms import *
from .models import *
from .mixin import *


# Create your views here.

class UserRegister(DataMixIn, CreateView):
    template_name = "register.html"
    form_class = RegisterForm

    def get(self, request, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.get_redirect_url())
        context = {
            'form': RegisterForm(),
            'title': 'Регистрация'
        }
        return render(request, self.template_name, context)

    def form_valid(self, form):
        email = form.cleaned_data['email']
        name = form.cleaned_data["name"]
        password = form.cleaned_data["password1"]
        MyUser.objects.create_user(email=email, name=name,
                              is_cooker=False, username=email, password = password)
        data = {
            'status': 200,
            'success': 'Вы успешно зарегистрировались',
        }
        return JsonResponse(data=data, status=200)

    def form_invalid(self, form):
        data = dict()
        data["error"] = list(form.errors.as_data().values())[0][0].message
        data["status"] = 400
        return JsonResponse(data=data, status=200)


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

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data["password"]
            if email and password:
                user = authenticate(username=email, password=password)
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
