



from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TenantViewSet, TenantResourceViewSet

router = DefaultRouter()
router.register(r'tenants', TenantViewSet)
router.register(r'tenant-resources', TenantResourceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]



from django.urls import path
from .views import TenantView

urlpatterns = [
    path('tenants/', TenantView.as_view(), name="tenants_list")
]
