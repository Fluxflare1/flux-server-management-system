// src/frontend/src/components/TenantManagement/TenantList.js
import React, { useState, useEffect } from 'react';

function TenantList() {
    const [tenants, setTenants] = useState([]);

    useEffect(() => {
        // Fetch tenants list from backend
    }, []);

    return (
        <div>
            <h2>Tenants</h2>
            <ul>
                {tenants.map(tenant => (
                    <li key={tenant.id}>{tenant.name}</li>
                ))}
            </ul>
        </div>
    );
}

export default TenantList;
