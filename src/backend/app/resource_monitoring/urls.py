# src/backend/app/resource_monitoring/urls.py
from django.urls import path
from .views import MetricsView

urlpatterns = [
    path("metrics/", MetricsView.as_view(), name="metrics"),
]
