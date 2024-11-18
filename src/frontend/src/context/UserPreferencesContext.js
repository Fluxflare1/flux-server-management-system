

import { useUserPreferences } from '../../context/UserPreferencesContext';

const Tooltip = ({ id, message }) => {
  const { tooltipsEnabled } = useUserPreferences();

  if (!tooltipsEnabled) return null;

  return (
    <>
      <span data-tip data-for={id}>ℹ️</span>
      <ReactTooltip id={id} place="top" effect="solid">
        {message}
      </ReactTooltip>
    </>
  );
};





// Path: frontend/src/context/UserPreferencesContext.js
import React, { createContext, useState, useContext } from 'react';

const UserPreferencesContext = createContext();

export const useUserPreferences = () => useContext(UserPreferencesContext);

export const UserPreferencesProvider = ({ children }) => {
  const [tooltipsEnabled, setTooltipsEnabled] = useState(true);

  return (
    <UserPreferencesContext.Provider value={{ tooltipsEnabled, setTooltipsEnabled }}>
      {children}
    </UserPreferencesContext.Provider>
  );
};
