

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivityLogViewSet

router = DefaultRouter()
router.register(r'activity-logs', ActivityLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]



from django.urls import path
from .views import AuditLogView

urlpatterns = [
    path('logs/', AuditLogView.as_view(), name="audit_logs")
]
