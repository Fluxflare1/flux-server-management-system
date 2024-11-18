// Path: frontend/src/components/CustomerDashboard/ActivityLogs.js
import React from 'react';

const ActivityLogs = ({ logs }) => {
  return (
    <div>
      <h3>Recent Activity</h3>
      <ul>
        {logs.map((log, index) => (
          <li key={index}>
            {log.timestamp} - {log.message}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ActivityLogs;
