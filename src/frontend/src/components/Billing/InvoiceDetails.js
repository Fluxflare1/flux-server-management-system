// src/frontend/src/components/Billing/InvoiceDetails.js
import React from 'react';

function InvoiceDetails({ invoice }) {
    return (
        <div>
            <h3>Invoice #{invoice.id}</h3>
            <p>Date: {invoice.date}</p>
            <p>Status: {invoice.status}</p>
            <p>Amount: ${invoice.amount}</p>
            {/* Payment button component */}
        </div>
    );
}

export default InvoiceDetails;
