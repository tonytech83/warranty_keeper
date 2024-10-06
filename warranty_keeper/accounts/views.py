from django.contrib.auth import views as auth_views, get_user_model, logout
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views import generic as views

from warranty_keeper.accounts.forms import LoginUserForm, UserRegistrationForm

UserModel = get_user_model()


class LoginView(auth_views.LoginView):
    form_class = LoginUserForm
    template_name = "accounts/login-page.html"  # TODO: fix template

    # TODO: To fullfil `success_url`
    success_url = reverse_lazy()


def logout_user(request):
    logout(request)

    return redirect('home-page')


class RegisterUserView(views.CreateView):
    queryset = UserModel.objects.all()
    template_name = "accounts/register-page.html"  # TODO: fix template
    form_class = UserRegistrationForm

    # TODO: To fullfil `success_url`
    success_url = reverse_lazy()


class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = "accounts/password_change_form.html" # TODO: fix template
    success_url = reverse_lazy("password_change_done") # TODO: fix success_url

