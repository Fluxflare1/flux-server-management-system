







from django.urls import path
from .views import TenantView

urlpatterns = [
    path('tenants/', TenantView.as_view(), name="tenants_list")
]
