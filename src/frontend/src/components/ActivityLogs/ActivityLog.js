// src/frontend/src/components/ActivityLog/ActivityLog.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import ActivityLogFilter from './ActivityLogFilter';

const ActivityLog = () => {
    const [logs, setLogs] = useState([]);
    const [filter, setFilter] = useState({});

    useEffect(() => {
        fetchLogs(filter);
    }, [filter]);

    const fetchLogs = async (filter) => {
        const response = await axios.get('/api/activity-log', { params: filter });
        setLogs(response.data);
    };

    return (
        <div>
            <h2>Activity Logs</h2>
            <ActivityLogFilter setFilter={setFilter} />
            <table>
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>User</th>
                        <th>Action</th>
                        <th>Details</th>
                    </tr>
                </thead>
                <tbody>
                    {logs.map((log) => (
                        <tr key={log.id}>
                            <td>{log.date}</td>
                            <td>{log.user}</td>
                            <td>{log.action}</td>
                            <td>{log.details}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default ActivityLog;
