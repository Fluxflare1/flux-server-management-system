// ServerConfigPanel.js - React component for advanced server configuration

import React, { useState } from 'react';

function ServerConfigPanel() {
  const [config, setConfig] = useState({
    djangoChannels: false,
    websocketSupport: false,
  });

  const handleConfigChange = (e) => {
    const { name, checked } = e.target;
    setConfig({ ...config, [name]: checked });
  };

  const applyConfig = () => {
    console.log("Applying configuration:", config);
    // Code to send configuration to backend for processing
  };

  return (
    <div>
      <h2>Advanced Server Configuration</h2>
      <label>
        <input
          type="checkbox"
          name="djangoChannels"
          checked={config.djangoChannels}
          onChange={handleConfigChange}
        />
        Enable Django Channels
      </label>
      <label>
        <input
          type="checkbox"
          name="websocketSupport"
          checked={config.websocketSupport}
          onChange={handleConfigChange}
        />
        Enable WebSocket Support
      </label>
      <button onClick={applyConfig}>Apply Configuration</button>
    </div>
  );
}

export default ServerConfigPanel;
