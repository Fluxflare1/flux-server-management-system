


from rest_framework import viewsets
from .models import Tenant, TenantResource
from .serializers import TenantSerializer, TenantResourceSerializer
from rest_framework.permissions import IsAuthenticated

class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [IsAuthenticated]

class TenantResourceViewSet(viewsets.ModelViewSet):
    queryset = TenantResource.objects.all()
    serializer_class = TenantResourceSerializer
    permission_classes = [IsAuthenticated]





from django.urls import path
from .views import TenantView

urlpatterns = [
    path('tenants/', TenantView.as_view(), name="tenants_list")
]
