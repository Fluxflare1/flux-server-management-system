// src/frontend/components/admin/CustomRolesManager.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';

const CustomRolesManager = () => {
    const [roles, setRoles] = useState([]);
    const [newRole, setNewRole] = useState({ name: '', permissions: [] });

    useEffect(() => {
        // Fetch existing roles
        axios.get('/api/admin/custom-roles').then(response => setRoles(response.data));
    }, []);

    const handleCreateRole = () => {
        axios.post('/api/admin/custom-roles', newRole).then(response => {
            setRoles([...roles, response.data]);
            setNewRole({ name: '', permissions: [] });
        });
    };

    return (
        <div>
            <h2>Custom Roles Management</h2>
            {/* UI for role creation and listing */}
            <input
                type="text"
                placeholder="Role Name"
                value={newRole.name}
                onChange={e => setNewRole({ ...newRole, name: e.target.value })}
            />
            <button onClick={handleCreateRole}>Create Role</button>
            {/* List existing roles */}
            <ul>
                {roles.map((role, index) => (
                    <li key={index}>{role.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default CustomRolesManager;
