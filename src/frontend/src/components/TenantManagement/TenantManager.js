// frontend/src/components/Tenant/TenantManager.js
import React, { useEffect, useState } from 'react';
import { getTenants, updateTenant } from '../../services/tenantService';

const TenantManager = () => {
    const [tenants, setTenants] = useState([]);

    useEffect(() => {
        getTenants()
            .then(response => setTenants(response.data))
            .catch(() => alert('Failed to load tenants'));
    }, []);

    const handleUpdateTenant = (tenantId) => {
        updateTenant(tenantId)
            .then(() => alert('Tenant updated'))
            .catch(() => alert('Failed to update tenant'));
    };

    return (
        <div>
            <h2>Tenant Management</h2>
            <ul>
                {tenants.map(tenant => (
                    <li key={tenant.id}>
                        <p>{tenant.name}</p>
                        <button onClick={() => handleUpdateTenant(tenant.id)}>Update</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default TenantManager;
