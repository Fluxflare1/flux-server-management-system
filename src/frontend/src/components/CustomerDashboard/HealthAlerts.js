// Path: frontend/src/components/CustomerDashboard/HealthAlerts.js
import React from 'react';

const HealthAlerts = ({ alerts }) => {
  return (
    <div>
      <h3>Health Alerts</h3>
      <ul>
        {alerts.map((alert, index) => (
          <li key={index} style={{ color: alert.critical ? 'red' : 'orange' }}>
            {alert.message}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default HealthAlerts;
