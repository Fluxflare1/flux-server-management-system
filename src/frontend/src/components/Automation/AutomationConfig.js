// frontend/src/components/Automation/AutomationConfig.js
import React, { useState } from 'react';
import { autoRegisterDomain, suspendDomain, terminateAccount } from '../../services/automationService';

const AutomationConfig = () => {
    const [domainName, setDomainName] = useState('');
    const [accountId, setAccountId] = useState('');
    const [message, setMessage] = useState('');

    const handleAutoRegister = () => {
        autoRegisterDomain(domainName)
            .then(() => setMessage('Domain registered automatically'))
            .catch(() => setMessage('Failed to register domain automatically'));
    };

    const handleSuspend = () => {
        suspendDomain(domainName)
            .then(() => setMessage('Domain suspended'))
            .catch(() => setMessage('Failed to suspend domain'));
    };

    const handleTerminate = () => {
        terminateAccount(accountId)
            .then(() => setMessage('Account terminated'))
            .catch(() => setMessage('Failed to terminate account'));
    };

    return (
        <div>
            <h2>Automation Configuration</h2>
            <input value={domainName} onChange={(e) => setDomainName(e.target.value)} placeholder="Enter domain" />
            <button onClick={handleAutoRegister}>Auto Register Domain</button>
            <button onClick={handleSuspend}>Suspend Domain</button>
            <br />
            <input value={accountId} onChange={(e) => setAccountId(e.target.value)} placeholder="Enter account ID" />
            <button onClick={handleTerminate}>Terminate Account</button>
            {message && <p>{message}</p>}
        </div>
    );
};

export default AutomationConfig;
