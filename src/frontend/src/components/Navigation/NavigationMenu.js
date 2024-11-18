

// Path: frontend/src/components/Navigation/NavigationMenu.js
import React from 'react';

const NavigationMenu = ({ userRole }) => {
  const menuItems = {
    admin: ['Dashboard', 'Server Management', 'Billing', 'Monitoring', 'Settings'],
    user: ['Dashboard', 'Server Management', 'Billing'],
  };

  return (
    <nav className="navigation-menu">
      <ul>
        {menuItems[userRole].map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </nav>
  );
};

export default NavigationMenu;





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
