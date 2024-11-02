# src/backend/app/version_control/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import git
import os

REPO_PATH = "/path/to/cloned/repo"  # Adjust this path as needed

class CloneRepoView(APIView):
    def post(self, request):
        repo_url = request.data.get('repo_url')
        git.Repo.clone_from(repo_url, REPO_PATH)
        return Response({"message": "Repository cloned"}, status=status.HTTP_201_CREATED)

class PullRepoView(APIView):
    def post(self, request):
        repo = git.Repo(REPO_PATH)
        repo.git.pull()
        return Response({"message": "Repository updated"}, status=status.HTTP_200_OK)

class RepoStatusView(APIView):
    def get(self, request):
        repo = git.Repo(REPO_PATH)
        return Response({"status": repo.git.status()}, status=status.HTTP_200_OK)
