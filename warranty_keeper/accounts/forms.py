from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class LoginUserForm(auth_forms.AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ("email", "password")


class UserRegistrationForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("email",)
