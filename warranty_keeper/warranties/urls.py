from django.urls import path

from warranty_keeper.warranties.views import WarrantiesView

urlpatterns = (
    path("", WarrantiesView.as_view(), name="warranty-list"),
)
