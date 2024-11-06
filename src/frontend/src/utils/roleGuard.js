// src/frontend/utils/roleGuard.js

import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const roleGuard = (userRole, requiredRole) => {
    const navigate = useNavigate();
    
    useEffect(() => {
        if (userRole !== requiredRole) {
            navigate('/unauthorized'); // Redirect to an unauthorized access page
        }
    }, [userRole, requiredRole, navigate]);
};

export default roleGuard;
