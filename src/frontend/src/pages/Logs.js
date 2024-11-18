// Path: frontend/src/pages/Logs.js
import React, { useState } from 'react';
import Filter from '../components/Search/Filter';

const Logs = ({ logs }) => {
  const [filteredLogs, setFilteredLogs] = useState(logs);

  const handleFilterChange = (filter) => {
    const newLogs = logs.filter((log) => log.type === filter);
    setFilteredLogs(newLogs);
  };

  return (
    <div>
      <Filter
        options={[
          { label: 'All', value: 'all' },
          { label: 'Error', value: 'error' },
          { label: 'Info', value: 'info' },
        ]}
        onFilterChange={handleFilterChange}
      />
      <ul>
        {filteredLogs.map((log, index) => (
          <li key={index}>{log.message}</li>
        ))}
      </ul>
    </div>
  );
};

export default Logs;
