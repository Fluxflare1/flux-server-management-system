// frontend/src/components/Backup/BackupManager.js
import React, { useState } from 'react';
import { initiateBackup, restoreBackup } from '../../services/backupService';

const BackupManager = () => {
    const [message, setMessage] = useState('');

    const handleBackup = () => {
        initiateBackup()
            .then(() => setMessage('Backup created successfully'))
            .catch(() => setMessage('Failed to create backup'));
    };

    const handleRestore = () => {
        restoreBackup()
            .then(() => setMessage('Backup restored successfully'))
            .catch(() => setMessage('Failed to restore backup'));
    };

    return (
        <div>
            <h2>Backup and Recovery</h2>
            <button onClick={handleBackup}>Create Backup</button>
            <button onClick={handleRestore}>Restore Backup</button>
            {message && <p>{message}</p>}
        </div>
    );
};

export default BackupManager;
