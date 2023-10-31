from django.urls import path

from .views import *

urlpatterns = [
    path('', UserLogin.as_view(), name="login"),
    path('registration/', UserRegister.as_view(), name='register'),
    path('logout', logout_user, name="logout")
]