


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet, PaymentViewSet, UsageRecordViewSet

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'usagerecords', UsageRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]




from django.urls import path
from .views import BillingView

urlpatterns = [
    path('billing/', BillingView.as_view(), name="billing_info")
]
