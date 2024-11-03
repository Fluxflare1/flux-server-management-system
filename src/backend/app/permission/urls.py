from django.urls import path
from .views import RoleView

urlpatterns = [
    path('roles/', RoleView.as_view(), name="roles_list")
]
