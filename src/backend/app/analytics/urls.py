

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnalyticsRecordViewSet

router = DefaultRouter()
router.register(r'analytics', AnalyticsRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]





from django.urls import path
from .views import AnalyticsView

urlpatterns = [
    path('analytics/', AnalyticsView.as_view(), name="analytics_reports")
]
