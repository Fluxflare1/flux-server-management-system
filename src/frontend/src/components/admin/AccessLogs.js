// src/frontend/components/admin/AccessLogs.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';

const AccessLogs = () => {
    const [logs, setLogs] = useState([]);

    useEffect(() => {
        // Fetch logs from backend
        axios.get('/api/admin/access-logs').then(response => {
            setLogs(response.data);
        });
    }, []);

    return (
        <div>
            <h2>Access Logs</h2>
            <table>
                <thead>
                    <tr>
                        <th>User ID</th>
                        <th>Role</th>
                        <th>Action</th>
                        <th>Resource</th>
                        <th>Status</th>
                        <th>Timestamp</th>
                    </tr>
                </thead>
                <tbody>
                    {logs.map((log, index) => (
                        <tr key={index}>
                            <td>{log.user_id}</td>
                            <td>{log.role}</td>
                            <td>{log.action}</td>
                            <td>{log.resource}</td>
                            <td>{log.status}</td>
                            <td>{new Date(log.timestamp).toLocaleString()}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default AccessLogs;
