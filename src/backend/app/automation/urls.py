from django.urls import path
from .views import AutomationView

urlpatterns = [
    path('automation/', AutomationView.as_view(), name="automation_tasks")
]
