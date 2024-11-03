
from django.urls import path
from .views import AutomationTasksView

urlpatterns = [
    path('automation_tasks/', AutomationTasksView.as_view(), name="automation_tasks")
]




from django.urls import path
from .views import AutomationView

urlpatterns = [
    path('automation/', AutomationView.as_view(), name="automation_tasks")
]
