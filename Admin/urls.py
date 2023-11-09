from django.urls import path

from .views import *
urlpatterns = [
    path('', CreateEmploy.as_view(), name="administrator")
]