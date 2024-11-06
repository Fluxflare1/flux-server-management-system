// src/frontend/components/Dashboard.js

import React from 'react';

const Dashboard = ({ role }) => (
    <div>
        <h1>Dashboard</h1>
        {role === 'Admin' || role === 'SuperAdmin' ? (
            <button onClick={() => window.location.href = '/user-management'}>User Management</button>
        ) : null}
        {role === 'SuperAdmin' ? (
            <button onClick={() => window.location.href = '/system-config'}>System Configuration</button>
        ) : null}
        <button onClick={() => window.location.href = '/analytics'}>Analytics</button>
    </div>
);

export default Dashboard;
