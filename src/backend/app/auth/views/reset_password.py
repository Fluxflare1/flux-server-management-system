# src/backend/app/auth/views/reset_password.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def reset_password_view(request, token):
    if request.method == 'POST':
        new_password = request.POST['new_password']
        # Verify token logic, and if valid:
        user = ...  # Fetch user by token
        user.set_password(new_password)
        user.save()
        messages.success(request, 'Password has been reset successfully!')
        return redirect('login')  # Redirect to login after resetting
    return render(request, 'auth/reset_password.html', {'token': token})
