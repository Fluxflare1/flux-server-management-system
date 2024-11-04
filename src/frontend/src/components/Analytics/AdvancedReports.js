// frontend/src/components/Analytics/AdvancedReports.js
import React, { useEffect, useState } from 'react';
import { getDetailedInsights, schedulePeriodicReports } from '../../services/analyticsService';

const AdvancedReports = () => {
    const [insights, setInsights] = useState([]);

    useEffect(() => {
        getDetailedInsights()
            .then(response => setInsights(response.userActivities))
            .catch(() => alert('Failed to load insights'));
    }, []);

    const handleScheduleReports = () => {
        schedulePeriodicReports()
            .then(() => alert('Reports scheduled successfully'))
            .catch(() => alert('Failed to schedule reports'));
    };

    return (
        <div>
            <h2>Advanced Analytics Reports</h2>
            <button onClick={handleScheduleReports}>Schedule Periodic Reports</button>
            <ul>
                {insights.map(insight => (
                    <li key={insight.id}>{insight.action}</li>
                ))}
            </ul>
        </div>
    );
};

export default AdvancedReports;
