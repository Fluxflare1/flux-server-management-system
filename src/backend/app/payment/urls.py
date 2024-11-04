# src/backend/app/payments/urls.py

from django.urls import path
from .views import InitializePaymentView, VerifyPaymentView

urlpatterns = [
    path("initialize/", InitializePaymentView.as_view(), name="initialize_payment"),
    path("verify/<str:reference>/", VerifyPaymentView.as_view(), name="verify_payment"),
]
