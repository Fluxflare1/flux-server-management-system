import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ActivityLog = () => {
  const [logs, setLogs] = useState([]);
  const [filter, setFilter] = useState({ startDate: '', endDate: '' });

  useEffect(() => {
    fetchLogs();
  }, []);

  const fetchLogs = async () => {
    try {
      const response = await axios.get('/api/logs', { params: filter });
      setLogs(response.data);
    } catch (error) {
      console.error('Error fetching logs:', error);
    }
  };

  const handleFilterChange = (e) => {
    setFilter({ ...filter, [e.target.name]: e.target.value });
  };

  const downloadLogs = () => {
    axios.get('/api/logs/download', { responseType: 'blob' })
      .then(response => {
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', 'activity_logs.csv');
        document.body.appendChild(link);
        link.click();
      });
  };

  return (
    <div>
      <h1>Activity Logs</h1>
      <input type="date" name="startDate" onChange={handleFilterChange} />
      <input type="date" name="endDate" onChange={handleFilterChange} />
      <button onClick={fetchLogs}>Filter Logs</button>
      <button onClick={downloadLogs}>Download Logs</button>
      <ul>
        {logs.map((log, index) => (
          <li key={index}>{log.message}</li>
        ))}
      </ul>
    </div>
  );
};

export default ActivityLog;
