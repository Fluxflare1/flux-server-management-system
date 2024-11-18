// Path: frontend/src/components/CustomerDashboard/ServerCard.js
import React from 'react';
import Tooltip from '../Tooltips/Tooltip';

const ServerCard = ({ server }) => {
  return (
    <div className="server-card">
      <h4>
        {server.name} <Tooltip id="server-name" message="This is your server's name." />
      </h4>
      <p>
        Status: {server.status} <Tooltip id="server-status" message="Current status of the server (e.g., Running, Stopped)." />
      </p>
    </div>
  );
};

export default ServerCard;
