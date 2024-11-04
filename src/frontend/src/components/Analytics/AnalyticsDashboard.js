// src/frontend/src/components/Analytics/AnalyticsDashboard.js
import React from 'react';
import UsageChart from './UsageChart';
import UserActivityChart from './UserActivityChart';

const AnalyticsDashboard = () => {
    return (
        <div>
            <h2>Analytics Dashboard</h2>
            <UsageChart />
            <UserActivityChart />
        </div>
    );
};

export default AnalyticsDashboard;
