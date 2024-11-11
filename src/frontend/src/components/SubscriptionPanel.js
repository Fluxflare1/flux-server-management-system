import React, { useState, useEffect } from 'react';

const SubscriptionPanel = () => {
  const [balance, setBalance] = useState(0);

  useEffect(() => {
    fetch('/api/user/balance')
      .then(response => response.json())
      .then(data => setBalance(data.balance));
  }, []);

  return (
    <div className="subscription-panel">
      <h3>Subscription Balance: ${balance}</h3>
    </div>
  );
};

export default SubscriptionPanel;
