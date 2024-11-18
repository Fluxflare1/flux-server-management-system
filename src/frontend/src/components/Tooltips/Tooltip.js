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
