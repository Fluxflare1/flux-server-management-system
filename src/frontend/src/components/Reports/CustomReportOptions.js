import React, { useState } from 'react';

function CustomReportOptions() {
    const [frequency, setFrequency] = useState('daily');
    const [format, setFormat] = useState('pdf');

    const handleGenerate = () => {
        // Logic to send options to the backend for report generation
    };

    return (
        <div>
            <select onChange={(e) => setFrequency(e.target.value)}>
                <option value="daily">Daily</option>
                <option value="weekly">Weekly</option>
            </select>
            <select onChange={(e) => setFormat(e.target.value)}>
                <option value="pdf">PDF</option>
                <option value="csv">CSV</option>
            </select>
            <button onClick={handleGenerate}>Generate Report</button>
        </div>
    );
}

export default CustomReportOptions;
