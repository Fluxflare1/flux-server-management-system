// src/frontend/components/Auth/TwoFactorAuth.js

import React, { useState } from 'react';

function TwoFactorAuth({ onSubmit }) {
    const [code, setCode] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit(code);
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Two-Factor Authentication</h2>
            <label>
                Enter the verification code sent to your email:
                <input
                    type="text"
                    value={code}
                    onChange={(e) => setCode(e.target.value)}
                    required
                />
            </label>
            <button type="submit">Verify</button>
        </form>
    );
}

export default TwoFactorAuth;
