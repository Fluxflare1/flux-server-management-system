# src/backend/app/middleware/rate_limiter.py
from flask import request, jsonify
from functools import wraps
import time

rate_limits = {}

def rate_limit(max_requests, window_seconds):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            user_ip = request.remote_addr
            current_time = time.time()
            user_requests = rate_limits.get(user_ip, [])
            user_requests = [t for t in user_requests if current_time - t < window_seconds]

            if len(user_requests) >= max_requests:
                return jsonify({'error': 'Rate limit exceeded'}), 429

            user_requests.append(current_time)
            rate_limits[user_ip] = user_requests
            return f(*args, **kwargs)
        return wrapped
    return decorator
