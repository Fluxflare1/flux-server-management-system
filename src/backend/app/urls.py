

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
