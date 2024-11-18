// Path: frontend/src/components/CustomerDashboard/MonitoringTools.js
import React from 'react';
import { Line } from 'react-chartjs-2';

const MonitoringTools = ({ historicalData }) => {
  const data = {
    labels: historicalData.timestamps,
    datasets: [
      {
        label: 'CPU Usage (%)',
        data: historicalData.cpu,
        borderColor: '#4caf50',
        fill: false,
      },
      {
        label: 'Memory Usage (GB)',
        data: historicalData.memory,
        borderColor: '#2196f3',
        fill: false,
      },
      {
        label: 'Storage Usage (GB)',
        data: historicalData.storage,
        borderColor: '#ff9800',
        fill: false,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: { position: 'bottom' },
    },
  };

  return (
    <div>
      <h3>Monitoring Tools</h3>
      <Line data={data} options={options} />
    </div>
  );
};

export default MonitoringTools;
