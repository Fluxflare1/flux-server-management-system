


# src/backend/auth/roles.py

ROLES = {
    'User': {
        'view': ['profile', 'billing', 'activity_log'],
        'edit': ['profile'],
    },
    'Admin': {
        'view': ['profile', 'billing', 'activity_log', 'user_management', 'analytics'],
        'edit': ['profile', 'billing', 'user_management', 'report_settings'],
        'schedule': ['analytics_reports'],
    },
    'SuperAdmin': {
        'view': ['profile', 'billing', 'activity_log', 'user_management', 'analytics', 'system_config'],
        'edit': ['profile', 'billing', 'user_management', 'analytics', 'system_config'],
        'delete': ['user_management'],
        'schedule': ['analytics_reports'],
    }
}





# src/backend/auth/roles.py

ROLES = {
    'User': {
        'view': ['profile', 'billing', 'activity_log'],
        'edit': ['profile'],
    },
    'Admin': {
        'view': ['profile', 'billing', 'activity_log', 'user_management', 'analytics'],
        'edit': ['profile', 'billing', 'user_management'],
    },
    'SuperAdmin': {
        'view': ['profile', 'billing', 'activity_log', 'user_management', 'analytics', 'system_config'],
        'edit': ['profile', 'billing', 'user_management', 'analytics', 'system_config'],
        'delete': ['user_management'],
    }
}
