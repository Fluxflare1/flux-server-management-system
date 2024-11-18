


// components/Dashboard.js

import React, { useEffect, useState } from 'react';
import { getServerList, fetchUserDetails } from '../services/apiService';

const Dashboard = () => {
  const [servers, setServers] = useState([]);
  const [user, setUser] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      try {
        const userDetails = await fetchUserDetails();
        setUser(userDetails.data);

        const serverList = await getServerList();
        setServers(serverList.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h1>Welcome, {user.name}</h1>
      <h2>Your Servers:</h2>
      <ul>
        {servers.map((server) => (
          <li key={server.id}>{server.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default Dashboard;




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
