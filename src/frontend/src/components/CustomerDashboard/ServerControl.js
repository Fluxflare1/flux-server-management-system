// Path: frontend/src/components/CustomerDashboard/ServerControl.js
import React from 'react';

const ServerControl = ({ serverStatus, onControlAction }) => {
  return (
    <div>
      <h3>Server Control Panel</h3>
      <p><strong>Current Status:</strong> {serverStatus}</p>
      <button onClick={() => onControlAction('start')}>Start Server</button>
      <button onClick={() => onControlAction('stop')}>Stop Server</button>
      <button onClick={() => onControlAction('restart')}>Restart Server</button>
    </div>
  );
};

export default ServerControl;
