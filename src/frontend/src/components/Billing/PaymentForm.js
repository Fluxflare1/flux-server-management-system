import React, { useState } from 'react';

function PaymentForm() {
    const [amount, setAmount] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        // Add payment processing logic here
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="number"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
                placeholder="Enter Amount"
            />
            <button type="submit">Pay</button>
        </form>
    );
}

export default PaymentForm;
