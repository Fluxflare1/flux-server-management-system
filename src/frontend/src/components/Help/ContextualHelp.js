// Path: frontend/src/components/Help/ContextualHelp.js
import React from 'react';

const ContextualHelp = ({ url, text }) => {
  return (
    <a href={url} target="_blank" rel="noopener noreferrer" className="help-button">
      {text || 'Learn More'}
    </a>
  );
};

export default ContextualHelp;
