# src/backend/app/user_management/urls.py
from django.urls import path
from .views import UserListView, UserDetailView

urlpatterns = [
    path("users/", UserListView.as_view(), name="user_list"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
]
