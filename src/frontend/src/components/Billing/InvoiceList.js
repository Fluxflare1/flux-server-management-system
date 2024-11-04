



// frontend/src/components/Billing/InvoiceList.js
import React, { useEffect, useState } from 'react';
import { getInvoices, makePayment } from '../../services/billingService';

const InvoiceList = () => {
    const [invoices, setInvoices] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        getInvoices()
            .then(response => setInvoices(response.data))
            .catch(err => setError('Failed to load invoices.'));
    }, []);

    const handlePayment = (invoiceId) => {
        makePayment(invoiceId)
            .then(() => alert('Payment successful'))
            .catch(() => alert('Payment failed'));
    };

    return (
        <div>
            <h2>Invoices</h2>
            {error && <p>{error}</p>}
            <ul>
                {invoices.map(invoice => (
                    <li key={invoice.id}>
                        <p>Invoice #{invoice.id} - ${invoice.amount}</p>
                        <button onClick={() => handlePayment(invoice.id)}>Pay Now</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default InvoiceList;




// src/frontend/src/components/Billing/InvoiceList.js
import React, { useEffect, useState } from 'react';

function InvoiceList() {
    const [invoices, setInvoices] = useState([]);

    useEffect(() => {
        // Fetch invoices from backend
    }, []);

    return (
        <div>
            <h2>Invoices</h2>
            <ul>
                {invoices.map(invoice => (
                    <li key={invoice.id}>
                        {invoice.date} - {invoice.status} - ${invoice.amount}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default InvoiceList;
