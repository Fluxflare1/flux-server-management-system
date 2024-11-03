import subprocess
from django.http import JsonResponse

def clone_repository(request):
    repo_url = request.GET.get('repo_url')
    if repo_url:
        try:
            subprocess.run(['git', 'clone', repo_url], check=True)
            return JsonResponse({'status': 'Repository cloned'}, status=201)
        except subprocess.CalledProcessError:
            return JsonResponse({'error': 'Cloning failed'}, status=500)
    return JsonResponse({'error': 'No repository URL provided'}, status=400)
