


import React from 'react';
import ServerStatus from './ServerStatus';
import SubscriptionPanel from './SubscriptionPanel';
import BackupRestorePanel from './BackupRestorePanel';

const Dashboard = () => {
  return (
    <div className="dashboard-container">
      <h2>Control Panel Dashboard</h2>
      <ServerStatus />
      <SubscriptionPanel />
      <BackupRestorePanel />
    </div>
  );
};

export default Dashboard;




// src/frontend/components/Dashboard.js

import React from 'react';

const Dashboard = ({ role }) => {
    const adminFeatures = role === 'Admin' || role === 'SuperAdmin';
    const superAdminFeatures = role === 'SuperAdmin';

    return (
        <div>
            <h1>Dashboard</h1>
            <button onClick={() => window.location.href = '/profile'}>Profile</button>
            <button onClick={() => window.location.href = '/billing'}>Billing</button>
            {adminFeatures && (
                <>
                    <button onClick={() => window.location.href = '/user-management'}>User Management</button>
                    <button onClick={() => window.location.href = '/analytics'}>Analytics</button>
                    <button onClick={() => window.location.href = '/report-settings'}>Report Settings</button>
                </>
            )}
            {superAdminFeatures && (
                <button onClick={() => window.location.href = '/system-config'}>System Configuration</button>
            )}
        </div>
    );
};

export default Dashboard;




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
