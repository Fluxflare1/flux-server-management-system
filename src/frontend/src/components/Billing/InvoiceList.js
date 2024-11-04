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
