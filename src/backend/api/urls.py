from django.urls import path
from .views.system_health import system_health_view

urlpatterns = [
    path('system-health/', system_health_view, name='system-health'),
]
