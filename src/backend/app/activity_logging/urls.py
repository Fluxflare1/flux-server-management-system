from django.urls import path
from .views import ActivityLogView

urlpatterns = [
    path('activity_logs/', ActivityLogView.as_view(), name="activity_logs")
]
