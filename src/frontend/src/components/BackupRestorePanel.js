import React from 'react';

const BackupRestorePanel = () => {
  const handleBackup = () => {
    fetch('/api/backup', { method: 'POST' });
  };

  const handleRestore = () => {
    fetch('/api/restore', { method: 'POST' });
  };

  return (
    <div className="backup-restore-panel">
      <h3>Backup & Restore</h3>
      <button onClick={handleBackup}>Create Backup</button>
      <button onClick={handleRestore}>Restore Backup</button>
    </div>
  );
};

export default BackupRestorePanel;
