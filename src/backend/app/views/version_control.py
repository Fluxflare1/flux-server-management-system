# src/backend/app/views/version_control.py
import git
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class VersionControlView(APIView):
    def post(self, request):
        """Clone a Git repository."""
        repo_url = request.data.get("repo_url")
        clone_dir = "/path/to/clone"
        try:
            git.Repo.clone_from(repo_url, clone_dir)
            return Response({"message": "Repository cloned successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
