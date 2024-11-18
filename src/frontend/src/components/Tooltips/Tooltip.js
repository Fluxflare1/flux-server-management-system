


<Tooltip id="server-name" contextKey="server_name" />
<Tooltip id="server-status" contextKey="server_status" />





// Path: frontend/src/components/Tooltips/Tooltip.js
import React, { useState, useEffect } from 'react';
import ReactTooltip from 'react-tooltip';

const Tooltip = ({ id, contextKey }) => {
  const [message, setMessage] = useState('');

  useEffect(() => {
    // Simulating an API call or data fetch for tooltip messages
    const fetchTooltipMessage = async () => {
      const tooltipMessages = {
        server_name: "This is your server's name.",
        server_status: "Current status of the server (e.g., Running, Stopped).",
      };
      setMessage(tooltipMessages[contextKey] || 'Tooltip not found.');
    };

    fetchTooltipMessage();
  }, [contextKey]);

  return (
    <>
      <span data-tip data-for={id}>ℹ️</span>
      <ReactTooltip id={id} place="top" effect="solid">
        {message}
      </ReactTooltip>
    </>
  );
};

export default Tooltip;




// Path: frontend/src/components/Tooltips/Tooltip.js
import React from 'react';
import ReactTooltip from 'react-tooltip';

const Tooltip = ({ id, message }) => {
  return (
    <>
      <span data-tip data-for={id}>ℹ️</span>
      <ReactTooltip id={id} place="top" effect="solid">
        {message}
      </ReactTooltip>
    </>
  );
};

export default Tooltip;
