// Path: frontend/src/pages/AdminDashboard.js
import React, { useState, useEffect } from 'react';
import SystemHealth from '../components/AdminDashboard/SystemHealth';
import Notifications from '../components/AdminDashboard/Notifications';
import ResourceSummary from '../components/AdminDashboard/ResourceSummary';

const AdminDashboard = () => {
  const [systemStats, setSystemStats] = useState({
    cpuUsage: [30, 40, 45, 50],
    memoryUsage: [60, 65, 70, 75],
    storageUsage: [50, 55, 60, 65],
  });

  const [resources, setResources] = useState([
    { client: 'Client A', cpu: 20, memory: 8, storage: 200 },
    { client: 'Client B', cpu: 30, memory: 16, storage: 500 },
  ]);

  return (
    <div>
      <h1>Admin Dashboard</h1>
      <SystemHealth {...systemStats} />
      <Notifications />
      <ResourceSummary resources={resources} />
    </div>
  );
};

export default AdminDashboard;
