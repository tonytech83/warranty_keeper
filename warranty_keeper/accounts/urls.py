from django.urls import path

from warranty_keeper.accounts.views import LoginView, logout_user, RegisterUserView, PasswordChangeView

urlpatterns = (
  path('login/', LoginView.as_view(), name='login-user'),
  path('register/', RegisterUserView.as_view(), name='register-user'),
  path('logout/', logout_user, name='logout-user'),
)
