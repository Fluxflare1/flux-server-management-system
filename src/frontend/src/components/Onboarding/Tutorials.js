// Path: frontend/src/components/Onboarding/Tutorials.js
import React from 'react';

const Tutorials = ({ onComplete }) => {
  return (
    <div>
      <h3>Interactive Tutorials</h3>
      <button onClick={() => onComplete('howToStartServer')}>
        How to Start a Server
      </button>
      <button onClick={() => onComplete('howToMonitorUsage')}>
        How to Monitor Usage
      </button>
    </div>
  );
};

export default Tutorials;
