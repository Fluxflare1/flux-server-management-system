// Path: frontend/src/components/CustomerDashboard/ResourceUsage.js
import React from 'react';
import { Bar } from 'react-chartjs-2';

const ResourceUsage = ({ cpuUsage, memoryUsage, storageUsage }) => {
  const data = {
    labels: ['CPU Usage (%)', 'Memory Usage (GB)', 'Storage Usage (GB)'],
    datasets: [
      {
        label: 'Usage',
        data: [cpuUsage, memoryUsage, storageUsage],
        backgroundColor: ['#4caf50', '#2196f3', '#ff9800'],
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: { display: false },
    },
  };

  return (
    <div>
      <h3>Resource Usage Overview</h3>
      <Bar data={data} options={options} />
    </div>
  );
};

export default ResourceUsage;
