import React, { useState, useEffect } from 'react';
import axios from 'axios';

function UserDashboard() {
    const [servers, setServers] = useState([]);
    const [balance, setBalance] = useState(0);

    useEffect(() => {
        axios.get('/api/user/servers')
            .then(response => setServers(response.data));

        axios.get('/api/user/balance')
            .then(response => setBalance(response.data.balance));
    }, []);

    return (
        <div>
            <h2>Your Dashboard</h2>
            <p>Balance: ${balance.toFixed(2)}</p>
            <h3>Your Servers</h3>
            <ul>
                {servers.map(server => (
                    <li key={server.id}>{server.name} - {server.status}</li>
                ))}
            </ul>
        </div>
    );
}

export default UserDashboard;
