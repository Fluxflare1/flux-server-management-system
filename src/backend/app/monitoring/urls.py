from django.urls import path
from . import monitoring_views

urlpatterns = [
    path('metrics/', monitoring_views.system_metrics, name='system_metrics'),
]
