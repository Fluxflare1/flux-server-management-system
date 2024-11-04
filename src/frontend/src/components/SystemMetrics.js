// src/frontend/src/components/SystemMetrics.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function SystemMetrics() {
    const [metrics, setMetrics] = useState({});

    useEffect(() => {
        axios.get('/api/metrics')
            .then(response => setMetrics(response.data))
            .catch(error => console.error(error));
    }, []);

    return (
        <div>
            <h2>System Metrics</h2>
            <p>CPU Usage: {metrics.cpu}%</p>
            <p>Memory Usage: {metrics.memory}%</p>
            <p>Storage Usage: {metrics.storage}%</p>
        </div>
    );
}

export default SystemMetrics;
