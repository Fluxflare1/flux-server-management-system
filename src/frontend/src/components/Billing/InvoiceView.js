

import React from 'react';

function InvoiceView() {
    return (
        <div>
            <h2>Your Invoices</h2>
            {/* Render invoices list here */}
        </div>
    );
}

export default InvoiceView;




import React from 'react';

function InvoiceView({ invoice }) {
    return (
        <div>
            <h3>Invoice for {invoice.billingPeriod}</h3>
            <p>Total Amount: ${invoice.amount}</p>
            <button>Pay Now</button>
        </div>
    );
}

export default InvoiceView;
