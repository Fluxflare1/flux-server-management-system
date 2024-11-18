

from .views.activity_logs import activity_logs_view

urlpatterns += [
    path('activity-logs/', activity_logs_view, name='activity-logs'),
]



from .views.notifications import notifications_view

urlpatterns += [
    path('notifications/', notifications_view, name='notifications'),
]



from .views.search import global_search_view

urlpatterns += [
    path('search/', global_search_view, name='global-search'),
]




from django.urls import path
from .views.system_health import system_health_view

urlpatterns = [
    path('system-health/', system_health_view, name='system-health'),
]
