import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import User
from django.http import JsonResponse

def generate_jwt(user):
    payload = {
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(hours=1),
        'iat': datetime.utcnow()
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

def decode_jwt(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return User.objects.get(id=payload['user_id'])
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, User.DoesNotExist):
        return None

def jwt_required(func):
    def wrapper(request, *args, **kwargs):
        token = request.headers.get('Authorization')
        if token:
            user = decode_jwt(token.split(" ")[1])
            if user:
                request.user = user
                return func(request, *args, **kwargs)
        return JsonResponse({'error': 'Unauthorized'}, status=401)
    return wrapper
