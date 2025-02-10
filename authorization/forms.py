from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth import password_validation, get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True)
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Пароль (повторно)", widget=forms.PasswordInput, help_text="Введите тот же самый пароль еще раз для проверки")

    class Meta:
        model = get_user_model()
        fields = ("email", "password1", "password2", "first_name", "last_name", "role")

    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        if password:
            password_validation.validate_password(password)
        return password

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Введенные пароли не совпадают", code="password_mismatch")
        return password2

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такая почта уже зарегистрирована!")
        return email
    


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.username = user.email  #действие для тлошл чтобы в случае авторизации через Create super user работа Вхлд
        user.is_active = True
        user.is_staff = True
        if commit:
            user.save()
        return user



class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "login__fields__username", "placeholder": "Email"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "login__fields__password", "placeholder": "Password"}
        )
    )

    class Meta:
        fields = ["username", "password"]
