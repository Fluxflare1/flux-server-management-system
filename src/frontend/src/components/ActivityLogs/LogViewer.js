

import React from 'react';

function LogViewer() {
    return (
        <div>
            <h2>Activity Log</h2>
            {/* Display activity logs here */}
        </div>
    );
}

export default LogViewer;



// frontend/src/components/ActivityLogs/LogViewer.js
import React, { useEffect, useState } from 'react';
import { getActivityLogs } from '../../services/logService';

const LogViewer = () => {
    const [logs, setLogs] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        getActivityLogs()
            .then(response => setLogs(response.data))
            .catch(() => setError('Failed to load activity logs.'));
    }, []);

    return (
        <div>
            <h2>Activity Logs</h2>
            {error && <p>{error}</p>}
            <ul>
                {logs.map(log => (
                    <li key={log.id}>
                        <p>{log.timestamp} - {log.action} by {log.user}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default LogViewer;
