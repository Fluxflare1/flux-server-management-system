import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { LineChart, Line, XAxis, YAxis, Tooltip, Legend, CartesianGrid } from 'recharts';

const AnalyticsDashboard = () => {
  const [analyticsData, setAnalyticsData] = useState([]);

  useEffect(() => {
    fetchAnalyticsData();
  }, []);

  const fetchAnalyticsData = async () => {
    try {
      const response = await axios.get('/api/analytics');
      setAnalyticsData(response.data);
    } catch (error) {
      console.error('Error fetching analytics data:', error);
    }
  };

  return (
    <div>
      <h1>Analytics Dashboard</h1>
      <LineChart width={600} height={300} data={analyticsData}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="date" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="usage" stroke="#8884d8" />
      </LineChart>
    </div>
  );
};

export default AnalyticsDashboard;
