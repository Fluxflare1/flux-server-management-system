// src/frontend/src/components/EmailConfigForm.js

import React, { useState } from 'react';

function EmailConfigForm() {
    const [formData, setFormData] = useState({
        emailBackend: '',
        emailHost: '',
        emailPort: '',
        emailUseTLS: false,
        emailUser: '',
        emailPassword: '',
    });

    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;
        setFormData({
            ...formData,
            [name]: type === 'checkbox' ? checked : value,
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        // Send formData to the backend to update settings
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>Email Backend</label>
            <input type="text" name="emailBackend" onChange={handleChange} />

            <label>Email Host</label>
            <input type="text" name="emailHost" onChange={handleChange} />

            <label>Email Port</label>
            <input type="number" name="emailPort" onChange={handleChange} />

            <label>Use TLS</label>
            <input type="checkbox" name="emailUseTLS" onChange={handleChange} />

            <label>Email User</label>
            <input type="text" name="emailUser" onChange={handleChange} />

            <label>Email Password</label>
            <input type="password" name="emailPassword" onChange={handleChange} />

            <button type="submit">Save Configuration</button>
        </form>
    );
}

export default EmailConfigForm;
