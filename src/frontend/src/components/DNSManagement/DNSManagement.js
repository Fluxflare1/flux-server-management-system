import React, { useState } from 'react';
import axios from 'axios';

const DNSManagement = () => {
    const [domainName, setDomainName] = useState('');
    const [clientID, setClientID] = useState('');

    const registerDomain = async () => {
        try {
            const response = await axios.post('/api/register-domain', { domain_name: domainName, client_id: clientID });
            alert(`Domain registered successfully: ${response.data.message}`);
        } catch (error) {
            alert(`Error: ${error.response.data.error}`);
        }
    };

    return (
        <div>
            <h1>DNS Management</h1>
            <input type="text" placeholder="Domain Name" value={domainName} onChange={e => setDomainName(e.target.value)} />
            <input type="text" placeholder="Client ID" value={clientID} onChange={e => setClientID(e.target.value)} />
            <button onClick={registerDomain}>Register Domain</button>
        </div>
    );
};

export default DNSManagement;
