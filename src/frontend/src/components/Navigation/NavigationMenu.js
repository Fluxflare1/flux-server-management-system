// Path: frontend/src/components/Navigation/NavigationMenu.js
import React, { useState } from 'react';

const NavigationMenu = () => {
  const [isCollapsed, setIsCollapsed] = useState(false);

  return (
    <nav className={`navigation-menu ${isCollapsed ? 'collapsed' : ''}`}>
      <button onClick={() => setIsCollapsed(!isCollapsed)}>
        {isCollapsed ? 'Expand' : 'Collapse'}
      </button>
      <ul>
        <li>Dashboard</li>
        <li>Server Management</li>
        <li>Billing</li>
        <li>Monitoring</li>
        <li>Settings</li>
      </ul>
    </nav>
  );
};

export default NavigationMenu;
