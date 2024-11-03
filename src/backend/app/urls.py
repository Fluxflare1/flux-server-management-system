



# src/backend/app/urls.py
from .views.user_management import UserViewSet, RoleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'roles', RoleViewSet)

urlpatterns += router.urls




# src/backend/app/urls.py
from .views.resource_monitoring import ResourceMonitoringView

urlpatterns += [
    path('metrics/', ResourceMonitoringView.as_view(), name='resource_metrics'),
]




# src/backend/app/urls.py
from django.urls import path
from .views.server_management import ServerManagementView

urlpatterns = [
    path('server/create/', ServerManagementView.as_view(), name='create_server'),
    path('server/<int:pk>/start/', ServerManagementView.as_view(), name='start_server'),
    path('server/<int:pk>/stop/', ServerManagementView.as_view(), name='stop_server'),
    path('server/<int:pk>/delete/', ServerManagementView.as_view(), name='delete_server'),
]





from django.urls import path, include

urlpatterns = [
    path('server/', include('app.server_management.urls')),
    path('monitoring/', include('app.monitoring.urls')),
    path('users/', include('app.user_management.urls')),
    path('version_control/', include('app.version_control.urls')),
]




from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




from django.urls import path
from .monitoring import views

urlpatterns = [
    path('health/', views.health_check),
]




# src/backend/app/urls.py
from django.urls import include, path

urlpatterns = [
    path("server-management/", include("app.server_management.urls")),
    path("resource-monitoring/", include("app.resource_monitoring.urls")),
    path("user-management/", include("app.user_management.urls")),
    path("version-control/", include("app.version_control.urls")),
]



from django.contrib import admin
from django.urls import path
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET"])
def home(request):
    return Response({"message": "Flux Server Management Backend Running"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
