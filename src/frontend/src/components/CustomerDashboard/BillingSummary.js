// Path: frontend/src/components/CustomerDashboard/BillingSummary.js
import React from 'react';

const BillingSummary = ({ currentBill, invoices, paymentMethod }) => {
  return (
    <div>
      <h3>Billing and Payment Summary</h3>
      <p><strong>Current Bill:</strong> ${currentBill}</p>
      <h4>Invoices</h4>
      <ul>
        {invoices.map((invoice, index) => (
          <li key={index}>
            {invoice.date} - ${invoice.amount} - {invoice.status}
          </li>
        ))}
      </ul>
      <h4>Payment Method</h4>
      <p>{paymentMethod}</p>
    </div>
  );
};

export default BillingSummary;
