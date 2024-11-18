import React, { useState, useEffect } from "react";
import { Line } from "react-chartjs-2";

const SystemHealthOverview = () => {
  const [healthData, setHealthData] = useState({
    cpu: [],
    memory: [],
    storage: [],
  });

  useEffect(() => {
    fetch("/api/system-health") // Update to the appropriate backend API path
      .then((res) => res.json())
      .then((data) => setHealthData(data))
      .catch((err) => console.error("Error fetching system health data:", err));
  }, []);

  const data = {
    labels: Array.from({ length: healthData.cpu.length }, (_, i) => `T-${i}`),
    datasets: [
      {
        label: "CPU Usage (%)",
        data: healthData.cpu,
        borderColor: "rgba(255, 99, 132, 1)",
        fill: false,
      },
      {
        label: "Memory Usage (%)",
        data: healthData.memory,
        borderColor: "rgba(54, 162, 235, 1)",
        fill: false,
      },
      {
        label: "Storage Usage (%)",
        data: healthData.storage,
        borderColor: "rgba(75, 192, 192, 1)",
        fill: false,
      },
    ],
  };

  return (
    <div className="system-health-overview">
      <h2>System Health Overview</h2>
      <Line data={data} />
    </div>
  );
};

export default SystemHealthOverview;
