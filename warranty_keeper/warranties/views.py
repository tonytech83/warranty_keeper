from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from warranty_keeper.warranties.models import Warranty

class WarrantiesView(auth_mixins.LoginRequiredMixin, views.ListView):
  queryset = Warranty.objects.all()
  template_name = 'warranties/warranty-list.html'
