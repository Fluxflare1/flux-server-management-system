// Path: frontend/src/components/CustomerDashboard/SupportTickets.js
import React, { useState } from 'react';

const SupportTickets = ({ tickets, onSubmitTicket }) => {
  const [newTicket, setNewTicket] = useState('');

  const handleSubmit = () => {
    onSubmitTicket(newTicket);
    setNewTicket('');
  };

  return (
    <div>
      <h3>Support Tickets</h3>
      <ul>
        {tickets.map((ticket, index) => (
          <li key={index}>
            {ticket.date} - {ticket.issue} - {ticket.status}
          </li>
        ))}
      </ul>
      <textarea
        value={newTicket}
        onChange={(e) => setNewTicket(e.target.value)}
        placeholder="Describe your issue..."
      />
      <button onClick={handleSubmit}>Submit Ticket</button>
    </div>
  );
};

export default SupportTickets;
