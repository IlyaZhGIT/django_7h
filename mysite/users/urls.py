from re import template
from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

from users.views import *

app_name = "users"

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(template_name="user/login.html"), name="login"),
    path(
        "logout/", LogoutView.as_view(template_name="user/logout.html"), name="logout"
    ),
]
