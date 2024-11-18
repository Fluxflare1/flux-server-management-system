// src/components/Onboarding/TwoFactorAuth.js

import React, { useState } from 'react';
import { generate2FA, verify2FA } from '../services/apiService';

const TwoFactorAuth = () => {
  const [otpUri, setOtpUri] = useState(null);
  const [code, setCode] = useState('');
  const [message, setMessage] = useState('');

  const handleGenerate = async () => {
    try {
      const { data } = await generate2FA();
      setOtpUri(data.otp_uri);
    } catch {
      setMessage('Error generating 2FA. Try again.');
    }
  };

  const handleVerify = async () => {
    try {
      const { data } = await verify2FA({ code });
      setMessage(data.detail);
    } catch {
      setMessage('Invalid code. Please try again.');
    }
  };

  return (
    <div>
      <button onClick={handleGenerate}>Generate 2FA</button>
      {otpUri && <p>Scan this QR Code with an authenticator app: {otpUri}</p>}

      <input
        type="text"
        placeholder="Enter 2FA Code"
        value={code}
        onChange={(e) => setCode(e.target.value)}
      />
      <button onClick={handleVerify}>Verify</button>

      {message && <p>{message}</p>}
    </div>
  );
};

export default TwoFactorAuth;
