import React, { useState, useEffect } from 'react';
import axios from 'axios';

function AdminDashboard() {
    const [users, setUsers] = useState([]);
    const [servers, setServers] = useState([]);

    useEffect(() => {
        axios.get('/api/admin/users')
            .then(response => setUsers(response.data));

        axios.get('/api/admin/servers')
            .then(response => setServers(response.data));
    }, []);

    return (
        <div>
            <h2>Admin Dashboard</h2>
            <h3>Users</h3>
            <ul>
                {users.map(user => (
                    <li key={user.id}>{user.username} - Balance: ${user.balance}</li>
                ))}
            </ul>

            <h3>All Servers</h3>
            <ul>
                {servers.map(server => (
                    <li key={server.id}>{server.name} - {server.status}</li>
                ))}
            </ul>
        </div>
    );
}

export default AdminDashboard;
