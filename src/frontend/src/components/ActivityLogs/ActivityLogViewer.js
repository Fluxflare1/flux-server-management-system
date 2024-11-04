// src/frontend/src/components/ActivityLogs/ActivityLogViewer.js
import React, { useEffect, useState } from 'react';

function ActivityLogViewer() {
    const [logs, setLogs] = useState([]);

    useEffect(() => {
        // Fetch activity logs from backend
    }, []);

    return (
        <div>
            <h2>Activity Logs</h2>
            <ul>
                {logs.map(log => (
                    <li key={log.id}>{log.message} - {log.timestamp}</li>
                ))}
            </ul>
        </div>
    );
}

export default ActivityLogViewer;
