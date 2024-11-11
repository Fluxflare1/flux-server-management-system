import React, { useState, useEffect } from 'react';

const ServerStatus = () => {
  const [status, setStatus] = useState([]);

  useEffect(() => {
    fetch('/api/server/status')
      .then(response => response.json())
      .then(data => setStatus(data));
  }, []);

  return (
    <div className="server-status-panel">
      <h3>Server Status</h3>
      <ul>
        {status.map(server => (
          <li key={server.id}>
            {server.name}: {server.cpuUsage}% CPU, {server.memoryUsage}% Memory
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ServerStatus;
