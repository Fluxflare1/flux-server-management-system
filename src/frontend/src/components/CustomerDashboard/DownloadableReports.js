// Path: frontend/src/components/CustomerDashboard/DownloadableReports.js
import React from 'react';

const DownloadableReports = () => {
  const handleDownload = () => {
    const data = 'Sample report data'; // Replace with dynamic data
    const blob = new Blob([data], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'usage_report.txt';
    link.click();
  };

  return (
    <div>
      <h3>Downloadable Reports</h3>
      <button onClick={handleDownload}>Download Usage Report</button>
    </div>
  );
};

export default DownloadableReports;
