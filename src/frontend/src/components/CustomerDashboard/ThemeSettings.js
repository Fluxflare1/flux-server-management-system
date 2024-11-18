// Path: frontend/src/components/CustomerDashboard/ThemeSettings.js
import React, { useState } from 'react';

const ThemeSettings = () => {
  const [darkMode, setDarkMode] = useState(false);

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
    document.body.className = darkMode ? '' : 'dark-mode';
  };

  return (
    <div>
      <h3>Theme Settings</h3>
      <button onClick={toggleDarkMode}>
        {darkMode ? 'Switch to Light Mode' : 'Switch to Dark Mode'}
      </button>
    </div>
  );
};

export default ThemeSettings;
