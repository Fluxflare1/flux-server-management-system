// src/frontend/src/components/Analytics/UsageChart.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';

const UsageChart = () => {
    const [usageData, setUsageData] = useState({});

    useEffect(() => {
        fetchUsageData();
    }, []);

    const fetchUsageData = async () => {
        const response = await axios.get('/api/analytics/usage');
        setUsageData(response.data);
    };

    const chartData = {
        labels: usageData.labels,
        datasets: [
            {
                label: 'CPU Usage (%)',
                data: usageData.cpu,
                borderColor: 'rgba(75,192,192,1)',
                fill: false,
            },
            {
                label: 'Memory Usage (%)',
                data: usageData.memory,
                borderColor: 'rgba(153,102,255,1)',
                fill: false,
            },
        ],
    };

    return <Line data={chartData} />;
};

export default UsageChart;
