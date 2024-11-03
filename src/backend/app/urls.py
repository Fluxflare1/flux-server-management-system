


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
