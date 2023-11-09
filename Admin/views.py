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

        for em in list(MyUser.objects.all().values("email")):
            if em['email'] == self.request.POST.get('email'):
                return JsonResponse(data={
                    'status': 400,
                    'error': "Учётная запись существует"
                }, status=200)
        print(self.request.POST.get('password1'))
        print(self.request.POST.get('password2'))
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
        MyUser.objects.create(email=email, name=name, password=password, is_cook=True)
        return JsonResponse(data={
            'status': 200,
            'success': 'Работник успешно добавлен',
        }, status=200)