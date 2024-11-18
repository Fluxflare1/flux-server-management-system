// Path: frontend/src/components/CustomerDashboard/QuickActions.js
import React from 'react';

const QuickActions = ({ onAction }) => {
  return (
    <div>
      <h3>Quick Actions</h3>
      <button onClick={() => onAction('startServer')}>Start Server</button>
      <button onClick={() => onAction('stopServer')}>Stop Server</button>
      <button onClick={() => onAction('createTicket')}>Create Ticket</button>
      <button onClick={() => onAction('upgradePlan')}>Upgrade Plan</button>
    </div>
  );
};

export default QuickActions;
