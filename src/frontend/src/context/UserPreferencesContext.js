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
