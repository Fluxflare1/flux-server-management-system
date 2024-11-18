// Path: frontend/src/components/Onboarding/WelcomeTour.js
import React from 'react';
import Joyride from 'react-joyride';

const WelcomeTour = () => {
  const steps = [
    {
      target: '.dashboard-overview',
      content: 'This is your dashboard overview.',
    },
    {
      target: '.quick-actions',
      content: 'Here are some quick actions to get started.',
    },
    {
      target: '.monitoring-tools',
      content: 'Monitor your server performance here.',
    },
  ];

  return <Joyride steps={steps} continuous={true} />;
};

export default WelcomeTour;
