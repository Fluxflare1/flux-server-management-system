# src/backend/app/views/admin.py
from utils.auth import role_required

@admin_bp.route('/manage_roles', methods=['POST'])
@role_required('admin')
def manage_roles():
    # logic to update roles
    return jsonify({'message': 'Roles updated successfully'})
