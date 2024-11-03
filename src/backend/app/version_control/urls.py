
from django.urls import path
from . import version_control_views

urlpatterns = [
    path('clone/', version_control_views.clone_repository, name='clone_repository'),
]



# src/backend/app/version_control/urls.py
from django.urls import path
from .views import CloneRepoView, PullRepoView, RepoStatusView

urlpatterns = [
    path("clone/", CloneRepoView.as_view(), name="clone_repo"),
    path("pull/", PullRepoView.as_view(), name="pull_repo"),
    path("status/", RepoStatusView.as_view(), name="repo_status"),
]
