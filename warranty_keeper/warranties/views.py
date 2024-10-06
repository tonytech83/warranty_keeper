from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from warranty_keeper.warranties.models import Warranty


class WarrantiesView(auth_mixins.LoginRequiredMixin, views.ListView):
    queryset = Warranty.objects.all()
    template_name = "warranties/warranty-list.html"


class DetailsWarrantyView(views.DetailView):
    pass


class WarrantyCreateView(views.CreateView):
    model = Warranty
    fields = ["name", "description", "invoice_img", "supplier"]
    template_name = "warranties/warranty-create.html"
    success_url = reverse_lazy(
        "warranty-list"
    )  # Adjust this to your desired redirect URL

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class WarrantyUpdateView(views.UpdateView):
    model = Warranty
    fields = ["name", "description", "invoice_img", "supplier"]
    template_name = "warranties/warranty_form.html"
    success_url = reverse_lazy("warranty-list")

    def get_queryset(self):
        return Warranty.objects.filter(owner=self.request.user)


class DeleteWarrantyView(views.DeleteView):
    pass
