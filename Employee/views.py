from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from Client.models import Order
# Create your views here.


class Employee(LoginRequiredMixin, View):
    template_name = "employee.html"

    def get(self, request):
        context = {
            "orders": Order.objects.filter(cooker = self.request.user, is_done=False).prefetch_related("order_id")
        }
        return render(request, self.template_name, context=context)

    def post(self, request):
        pk = self.request.POST.get("pk")
        print(pk)
        order = Order.objects.get(pk=pk)
        order.is_done = True

        return JsonResponse({'status': 200}, status = 400)


