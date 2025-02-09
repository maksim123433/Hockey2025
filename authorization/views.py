from debug_toolbar.panels.alerts import FormParser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView, FormView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from authorization.forms import LoginForm
from authorization.models import ProUser
from authorization.forms import RegisterUserForm


class RegisterView(CreateView):
    template_name = "authorization/authorization_form.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = "authorization/login.html"
    success_url = reverse_lazy("main")


