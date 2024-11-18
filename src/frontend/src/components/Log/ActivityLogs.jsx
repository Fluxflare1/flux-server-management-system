import React, { useState, useEffect } from "react";

const ActivityLogs = () => {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    fetch("/api/activity-logs")
      .then((res) => res.json())
      .then((data) => setLogs(data))
      .catch((err) => console.error("Error fetching activity logs:", err));
  }, []);

  return (
    <div className="activity-logs">
      <h2>Activity Logs</h2>
      <table>
        <thead>
          <tr>
            <th>User</th>
            <th>Action</th>
            <th>Timestamp</th>
          </tr>
        </thead>
        <tbody>
          {logs.map((log) => (
            <tr key={log.id}>
              <td>{log.user}</td>
              <td>{log.action}</td>
              <td>{new Date(log.timestamp).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ActivityLogs;
