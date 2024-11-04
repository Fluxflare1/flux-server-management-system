// src/frontend/src/components/Analytics/UserActivityChart.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Bar } from 'react-chartjs-2';

const UserActivityChart = () => {
    const [activityData, setActivityData] = useState({});

    useEffect(() => {
        fetchActivityData();
    }, []);

    const fetchActivityData = async () => {
        const response = await axios.get('/api/analytics/user-activity');
        setActivityData(response.data);
    };

    const chartData = {
        labels: activityData.labels,
        datasets: [
            {
                label: 'User Actions',
                data: activityData.actions,
                backgroundColor: 'rgba(54,162,235,0.6)',
            },
        ],
    };

    return <Bar data={chartData} />;
};

export default UserActivityChart;
