from django.views import generic as views
from django.contrib.auth.mixins import LoginRequiredMixin

from warranty_keeper.suppliers.models import Supplier


class SupplierListView(LoginRequiredMixin, views.ListView):
    model = Supplier
    template_name = "suppliers/suppliers-list.html"


class SupplierCreateView(views.CreateView):
    pass


class SupplierEditView(views.UpdateView):
    pass


class SupplierDeleteView(views.DeleteView):
    pass
