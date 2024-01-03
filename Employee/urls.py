from django.urls import path

from .views import *

urlpatterns = [
    path('', Employee.as_view(), name="employee"),
]