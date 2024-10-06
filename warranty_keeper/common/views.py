from django.views import generic as views
from django.contrib.auth import get_user_model

from warranty_keeper.warranties.models import Warranty

UserModel = get_user_model()

class HomePageView(views.ListView):
  queryset = (Warranty.objects.all())
  template_name = 'common/home-page.html'

class DashboardView(views.ListView):
  queryset = (Warranty.objects.all())
  template_name = 'common/dashboard.html'