from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from Auth.forms import RegisterForm
from Auth.models import *


# Create your views here.


class CreateEmploy(CreateView):
    template_name = 'administrator.html'
    form_class = RegisterForm

    @property
    def get_context_data(self, **kwargs):
        return {
            'title': "Регистрация работников",
            "form": RegisterForm(),
            'employees': MyUser.objects.filter(is_cooker=True)
        }

    def get(self, request, **kwargs):
        return render(request, self.template_name, context=self.get_context_data)

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('pk') is None:
            return super().post(request, *args, **kwargs)
        user = MyUser.objects.get(pk=self.request.POST.get("pk"))
        user.delete()
        return JsonResponse(data={'status': 200}, status=200)

    def form_valid(self, form):
        email = form.cleaned_data['email']
        name = form.cleaned_data["name"]
        password = form.cleaned_data["password1"]
        user = MyUser.objects.create_user(email=email, name=name,
                      is_cooker=True, username=email, password=password)

        return JsonResponse(data={
            'status': 200,
            'success': 'Работник успешно добавлен',
            "name": name,
            "email": email,
            'pk': user.pk
        }, status=200)

    def form_invalid(self, form):
        data = dict()
        data["error"] = list(form.errors.as_data().values())[0][0].message
        data["status"] = 400
        return JsonResponse(data=data, status=200)
