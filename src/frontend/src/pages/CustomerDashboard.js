// Path: frontend/src/pages/CustomerDashboard.js
import React, { useState } from 'react';
import ResourceUsage from '../components/CustomerDashboard/ResourceUsage';
import BillingSummary from '../components/CustomerDashboard/BillingSummary';
import ServerControl from '../components/CustomerDashboard/ServerControl';
import SupportTickets from '../components/CustomerDashboard/SupportTickets';

const CustomerDashboard = () => {
  const [resourceUsage] = useState({ cpuUsage: 70, memoryUsage: 16, storageUsage: 300 });
  const [billing] = useState({
    currentBill: 120.50,
    invoices: [
      { date: '2024-11-01', amount: 100, status: 'Paid' },
      { date: '2024-10-01', amount: 95, status: 'Paid' },
    ],
    paymentMethod: 'Visa **** 1234',
  });
  const [serverStatus, setServerStatus] = useState('Running');
  const [tickets, setTickets] = useState([
    { date: '2024-11-10', issue: 'Server downtime', status: 'Resolved' },
  ]);

  const handleControlAction = (action) => {
    console.log(`${action} server action initiated`);
    setServerStatus(action === 'stop' ? 'Stopped' : 'Running');
  };

  const handleSubmitTicket = (newTicket) => {
    const ticket = { date: new Date().toISOString().split('T')[0], issue: newTicket, status: 'Pending' };
    setTickets([...tickets, ticket]);
  };

  return (
    <div>
      <h1>Customer Dashboard</h1>
      <ResourceUsage {...resourceUsage} />
      <BillingSummary {...billing} />
      <ServerControl serverStatus={serverStatus} onControlAction={handleControlAction} />
      <SupportTickets tickets={tickets} onSubmitTicket={handleSubmitTicket} />
    </div>
  );
};

export default CustomerDashboard;
