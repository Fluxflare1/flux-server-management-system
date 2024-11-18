// Path: frontend/src/components/CustomerDashboard/CustomizableWidgets.js
import React, { useState } from 'react';
import ResourceUsage from './ResourceUsage';
import BillingSummary from './BillingSummary';
import ServerControl from './ServerControl';
import SupportTickets from './SupportTickets';

const CustomizableWidgets = ({ resourceUsage, billing, serverStatus, tickets }) => {
  const [layout, setLayout] = useState(['ResourceUsage', 'BillingSummary', 'ServerControl', 'SupportTickets']);

  const renderWidget = (widget) => {
    switch (widget) {
      case 'ResourceUsage':
        return <ResourceUsage {...resourceUsage} />;
      case 'BillingSummary':
        return <BillingSummary {...billing} />;
      case 'ServerControl':
        return <ServerControl serverStatus={serverStatus} />;
      case 'SupportTickets':
        return <SupportTickets tickets={tickets} />;
      default:
        return null;
    }
  };

  return (
    <div>
      <h3>Customizable Widgets</h3>
      {layout.map((widget, index) => (
        <div key={index} draggable>
          {renderWidget(widget)}
        </div>
      ))}
    </div>
  );
};

export default CustomizableWidgets;
