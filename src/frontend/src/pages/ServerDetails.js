// Path: frontend/src/pages/ServerDetails.js
import React from 'react';
import Breadcrumb from '../components/Navigation/Breadcrumb';

const ServerDetails = () => {
  const breadcrumbPaths = [
    { label: 'Dashboard', url: '/' },
    { label: 'Servers', url: '/servers' },
    { label: 'Server Details', url: '/servers/123' },
  ];

  return (
    <div>
      <Breadcrumb paths={breadcrumbPaths} />
      <h1>Server Details</h1>
    </div>
  );
};

export default ServerDetails;
