import json
from random import choice

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F, Sum
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from .models import *


# Create your views here.

class HomePage(LoginRequiredMixin, View):
    template_name = "homepage.html"
    login_url = 'login'

    def get(self, request):
        context = {
            "menu": Chapter.objects.all().prefetch_related("get_menu"),
            "title": "Меню"
        }

        return render(request, self.template_name, context)

    def post(self, request):
        count = self.request.POST.get("count")
        name = self.request.POST.get("name")
        item_of_menu = Menu.objects.get()
        OrdersItem.objects.create(user_id=self.request.user,
                                  item=item_of_menu,
                                  count=count,
                                  is_selected=True,
                                  is_ordered = False)
        return JsonResponse({
            'status': 200,
            'message': "Всё прошло успешно"
        }, status=200)


class Basket(LoginRequiredMixin, View):
    template_name = "basket.html"
    login_url = 'login'

    def get_context_data(self):
        context = {
            'title': "Корзина заказа",
            "items": OrdersItem.objects.filter(user_id=self.request.user, is_ordered=False).annotate(
                total=F('count') * F('item__price')),
            "summ": OrdersItem.objects.filter(user_id=self.request.user, is_selected=True, is_ordered=False).aggregate(
                summ=Sum(F("count") * F("item__price")))['summ']
        }
        return context

    def get(self, request):
        context = self.get_context_data()
        if context['summ'] is None:
            context['summ'] = 0
        return render(request, self.template_name, context)

    def delete_item(self, request):
        pk = self.request.POST.get('pk')
        OrdersItem.objects.get(pk=pk).delete()
        summ = OrdersItem.objects.filter(user_id=self.request.user, is_selected=True, is_ordered=False).aggregate(
            summ=Sum(F("count") * F("item__price")))['summ']
        if summ is None:
            summ = 0
        return JsonResponse({
            'status': 200,
            'summ': summ
        }, status=200)

    def change_checkbox(self, request):
        pk = self.request.POST.get("pk")
        boolean = json.loads(self.request.POST.get("request"))
        item = OrdersItem.objects.get(pk=pk)
        item.is_selected = boolean
        item.save()
        summ = OrdersItem.objects.filter(user_id=self.request.user, is_selected=True, is_ordered=False).aggregate(
            summ=Sum(F("count") * F("item__price")))['summ']
        if summ is None:
            summ = 0
        return JsonResponse({
            'status': 200,
            "value": json.dumps(boolean),
            "summ": summ
        }, status=200)

    def create_order(self, request):

        cooker = choice(MyUser.objects.filter(is_cooker=True))

        new_order = Order.objects.create(cooker = cooker)

        OrdersItem.objects.filter(user_id=self.request.user, is_selected=True, is_ordered = False).update(
            is_ordered=True,
            order_id=new_order,
        )

        summ = OrdersItem.objects.filter(user_id=self.request.user, is_selected=True, is_ordered=False).aggregate(
            summ=Sum(F("count") * F("item__price")))['summ']
        if summ is None:
            summ = 0
        return JsonResponse(data={"summ": summ}, status=200)

    choose_post = {
        "delete": delete_item,
        "change": change_checkbox,
        "order": create_order
    }

    def post(self, request):
        return self.choose_post[self.request.POST.get("message")](self, request)
