// frontend/src/components/Domain/DomainManager.js
import React, { useState } from 'react';
import { registerDomain, renewDomain } from '../../services/domainService';

const DomainManager = () => {
    const [domainName, setDomainName] = useState('');
    const [message, setMessage] = useState('');

    const handleRegister = () => {
        registerDomain(domainName)
            .then(() => setMessage('Domain registered successfully'))
            .catch(() => setMessage('Failed to register domain'));
    };

    const handleRenew = () => {
        renewDomain(domainName)
            .then(() => setMessage('Domain renewed successfully'))
            .catch(() => setMessage('Failed to renew domain'));
    };

    return (
        <div>
            <h2>Domain Management</h2>
            <input value={domainName} onChange={(e) => setDomainName(e.target.value)} placeholder="Enter domain" />
            <button onClick={handleRegister}>Register Domain</button>
            <button onClick={handleRenew}>Renew Domain</button>
            {message && <p>{message}</p>}
        </div>
    );
};

export default DomainManager;
