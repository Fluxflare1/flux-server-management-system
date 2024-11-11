from flask import Blueprint, request, jsonify
from .models import User, Subscription
from .utils import calculate_usage_cost

billing_bp = Blueprint('billing', __name__)

@billing_bp.route('/api/billing/deduct', methods=['POST'])
def deduct_balance():
    data = request.json
    user_id = data.get("user_id")
    usage = data.get("usage")  # e.g., {"cpu_hours": 10, "bandwidth_gb": 50}

    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    cost = calculate_usage_cost(usage)
    if user.balance < cost:
        return jsonify({"error": "Insufficient balance"}), 402

    user.balance -= cost
    db.session.commit()
    return jsonify({"new_balance": user.balance}), 200
