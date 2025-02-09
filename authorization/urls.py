from django.contrib.auth.views import LogoutView, PasswordChangeView
from django.urls import path
from .views import RegisterView, LoginUser

urlpatterns = [
    path("registration/", RegisterView.as_view(), name="authoriz"),
    path("login/", LoginUser.as_view(next_page="main"), name="login"),
    path("logout/", LogoutView.as_view(next_page="main"), name="logout"),
    path("passwordchange/", PasswordChangeView.as_view(), name="password_change"),
    path("", LoginUser.as_view(next_page="main"), name="login"), #чтобы заходила с 0
]
