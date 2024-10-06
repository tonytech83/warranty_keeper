from django.urls import path

from warranty_keeper.warranties.views import WarrantiesView, WarrantyCreateView, WarrantyUpdateView

urlpatterns = (
    path("", WarrantiesView.as_view(), name="warranty-list"),
    path('create/', WarrantyCreateView.as_view(), name='warranty-create'),
    path('<int:pk>/edit/', WarrantyUpdateView.as_view(), name='warranty-update'),
)
