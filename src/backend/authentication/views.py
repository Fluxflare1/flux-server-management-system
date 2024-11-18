# backend/authentication/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import pyotp

# Simulate database storage for demo purposes
user_2fa_secrets = {}

@api_view(['POST'])
def generate_2fa(request):
    user_id = request.user.id
    if user_id not in user_2fa_secrets:
        secret = pyotp.random_base32()
        user_2fa_secrets[user_id] = secret
        otp_uri = pyotp.totp.TOTP(secret).provisioning_uri(f"user-{user_id}@flux", issuer_name="Flux Server")
        return Response({"otp_uri": otp_uri}, status=status.HTTP_201_CREATED)
    return Response({"detail": "2FA already generated for user."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def verify_2fa(request):
    user_id = request.user.id
    code = request.data.get("code", "")
    secret = user_2fa_secrets.get(user_id, None)

    if secret and pyotp.TOTP(secret).verify(code):
        return Response({"detail": "2FA verified successfully!"}, status=status.HTTP_200_OK)

    return Response({"detail": "Invalid 2FA code."}, status=status.HTTP_400_BAD_REQUEST)