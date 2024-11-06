// src/frontend/components/security/MFAChallenge.js

import React, { useState } from 'react';

const MFAChallenge = ({ onVerify }) => {
    const [code, setCode] = useState('');

    const handleSubmit = () => {
        // Verify the MFA code entered by user
        onVerify(code);
    };

    return (
        <div>
            <h2>MFA Challenge</h2>
            <input
                type="text"
                placeholder="Enter MFA Code"
                value={code}
                onChange={e => setCode(e.target.value)}
            />
            <button onClick={handleSubmit}>Verify</button>
        </div>
    );
};

export default MFAChallenge;
