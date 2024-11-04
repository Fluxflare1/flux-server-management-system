from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth import login
from .forms import UserRegistrationForm, CompanyAccountForm, PersonalAccountForm
from .models import User, CompanyAccount, PersonalAccount
from django.urls import reverse

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            send_verification_email(user)
            return redirect('check_email')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def send_verification_email(user):
    verification_link = reverse('verify_email', args=[user.id])
    send_mail(
        'Account Verification',
        f'Click the link to verify your account: {verification_link}',
        'noreply@example.com',
        [user.email]
    )

def verify_email(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_verified = True
    user.save()
    login(request, user)
    return redirect('choose_account_type')
