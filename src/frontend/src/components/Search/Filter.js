// Path: frontend/src/components/Search/Filter.js
import React from 'react';

const Filter = ({ options, onFilterChange }) => {
  return (
    <select onChange={(e) => onFilterChange(e.target.value)}>
      {options.map((option, index) => (
        <option key={index} value={option.value}>
          {option.label}
        </option>
      ))}
    </select>
  );
};

export default Filter;
