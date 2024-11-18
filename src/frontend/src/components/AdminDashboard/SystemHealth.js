// Path: frontend/src/components/AdminDashboard/SystemHealth.js
import React from 'react';
import { Line } from 'react-chartjs-2';

const SystemHealth = ({ cpuUsage, memoryUsage, storageUsage }) => {
  const data = {
    labels: ['Last Hour', 'Last 30 mins', 'Last 15 mins', 'Now'],
    datasets: [
      {
        label: 'CPU Usage (%)',
        data: cpuUsage,
        borderColor: 'rgba(75,192,192,1)',
        fill: false,
      },
      {
        label: 'Memory Usage (%)',
        data: memoryUsage,
        borderColor: 'rgba(153,102,255,1)',
        fill: false,
      },
      {
        label: 'Storage Usage (%)',
        data: storageUsage,
        borderColor: 'rgba(255,159,64,1)',
        fill: false,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: { position: 'top' },
    },
  };

  return (
    <div>
      <h3>System Health Overview</h3>
      <Line data={data} options={options} />
    </div>
  );
};

export default SystemHealth;
