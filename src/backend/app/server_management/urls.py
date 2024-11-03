


from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_server, name='create_server'),
    path('<int:server_id>/start/', views.start_server, name='start_server'),
    path('<int:server_id>/stop/', views.stop_server, name='stop_server'),
    path('<int:server_id>/delete/', views.delete_server, name='delete_server'),
]




# src/backend/app/server_management/urls.py
from django.urls import path
from .views import CreateServerView, StartServerView, StopServerView, DeleteServerView

urlpatterns = [
    path("create/", CreateServerView.as_view(), name="create_server"),
    path("start/<int:pk>/", StartServerView.as_view(), name="start_server"),
    path("stop/<int:pk>/", StopServerView.as_view(), name="stop_server"),
    path("delete/<int:pk>/", DeleteServerView.as_view(), name="delete_server"),
]
