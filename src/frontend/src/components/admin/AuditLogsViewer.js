// src/frontend/components/admin/AuditLogsViewer.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';

const AuditLogsViewer = () => {
    const [logs, setLogs] = useState([]);

    useEffect(() => {
        // Fetch audit logs from backend
        axios.get('/api/admin/audit-logs').then(response => {
            setLogs(response.data);
        });
    }, []);

    return (
        <div>
            <h2>Audit Logs</h2>
            <table>
                <thead>
                    <tr>
                        <th>User ID</th>
                        <th>Action</th>
                        <th>Details</th>
                        <th>Timestamp</th>
                    </tr>
                </thead>
                <tbody>
                    {logs.map((log, index) => (
                        <tr key={index}>
                            <td>{log.user_id}</td>
                            <td>{log.action}</td>
                            <td>{log.details}</td>
                            <td>{new Date(log.timestamp).toLocaleString()}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default AuditLogsViewer;
