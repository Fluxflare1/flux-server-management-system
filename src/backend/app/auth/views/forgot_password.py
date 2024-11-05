# src/backend/app/auth/views/forgot_password.py

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib import messages
import uuid

def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
            token = uuid.uuid4()
            # Save token to user model or related model for password reset
            # send_mail logic
            send_mail(
                'Password Reset Request',
                f'Use this link to reset your password: http://example.com/reset_password/{token}/',
                'from@example.com',
                [email],
                fail_silently=False,
            )
            messages.success(request, 'Password reset link sent!')
        except User.DoesNotExist:
            messages.error(request, 'Email not found.')
    return render(request, 'auth/forgot_password.html')
