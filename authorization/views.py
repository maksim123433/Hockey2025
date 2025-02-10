from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


from authorization.forms import LoginForm
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


