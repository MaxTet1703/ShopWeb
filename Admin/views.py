from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from Auth.forms import RegisterForm
from Auth.models import *


# Create your views here.


class CreateEmploy(View):
    template_name = 'administrator.html'

    @property
    def get_context_data(self):
        return {
            'title': "Регистрация работников",
            "form": RegisterForm(),
            'employees': MyUser.objects.filter(is_cook=True)
        }

    def get(self, request):
        return render(request, self.template_name, context=self.get_context_data)

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            password1 = form.cleaned_data['password1']

            new_user = MyUser(email=email, name=name, password=password1, is_cook=True)
            new_user.save()

            return JsonResponse(data={
                'status': 200,
                'success': 'Работник успешно добавлен',
                "name": new_user.name,
                "email": new_user.email,
                'pk': new_user.pk
            }, status=200)

        else:
            email = self.request.POST("email")
            name = self.request.POST("name")
            password1 = self.request.POST("password1")
            password2 = self.request.POST("password2")
            error: str
            if MyUser.objects.filter(email=email):
                error = "Пользователь с такой почтой уже существует"
            elif password1 != password2:
                error = "Пароли не совпадают"
            elif not name:
                error = "Введите имя сотрудника"
            else:
                error = "Введите данные корректно"
            return JsonResponse(data={
                'status': 400,
                'error': error,
            }, status=200)