from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View


# Create your views here.


class Employee(LoginRequiredMixin, View):
    template_name = "employee.html"

    def get(self, request):
        return render(request, self.template_name)
