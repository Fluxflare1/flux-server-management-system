// frontend/src/components/Analytics/Reports.js
import React, { useState, useEffect } from 'react';
import { fetchReportData } from '../../services/analyticsService';
import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip } from 'recharts';

const Reports = () => {
    const [reportData, setReportData] = useState([]);

    useEffect(() => {
        fetchReportData()
            .then(response => setReportData(response.data))
            .catch(() => alert('Failed to load report data'));
    }, []);

    return (
        <div>
            <h2>Usage Reports</h2>
            <LineChart width={600} height={300} data={reportData}>
                <Line type="monotone" dataKey="usage" stroke="#8884d8" />
                <CartesianGrid stroke="#ccc" />
                <XAxis dataKey="date" />
                <YAxis />
                <Tooltip />
            </LineChart>
        </div>
    );
};

export default Reports;
