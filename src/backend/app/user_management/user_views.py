from django.http import JsonResponse
from django.contrib.auth.models import User

def create_user(request):
    # Logic to create a new user
    return JsonResponse({'status': 'User created'}, status=201)

def get_user(request, user_id):
    # Logic to retrieve user details
    return JsonResponse({'status': f'User {user_id} details'}, status=200)

def update_user(request, user_id):
    # Logic to update user details
    return JsonResponse({'status': f'User {user_id} updated'}, status=200)

def delete_user(request, user_id):
    # Logic to delete a user
    return JsonResponse({'status': f'User {user_id} deleted'}, status=200)
