from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('warranty_keeper.common.urls')),
    path('auth/', include('warranty_keeper.accounts.urls')),
    path('warranties/', include('warranty_keeper.warranties.urls')),
    path('suppliers/', include('warranty_keeper.suppliers.urls')),
]
