# src/backend/app/views/example.py
from middleware.rate_limiter import rate_limit

@user_bp.route('/example', methods=['GET'])
@rate_limit(5, 60)  # 5 requests per minute
def example_route():
    return jsonify({'message': 'Hello, this is a rate-limited route!'})
