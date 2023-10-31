from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name="user"),
    path('basket/', Basket.as_view(), name="basket")
]
