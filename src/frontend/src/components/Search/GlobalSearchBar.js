// Path: frontend/src/components/Search/GlobalSearchBar.js
import React, { useState } from 'react';

const GlobalSearchBar = ({ data, onSearchResult }) => {
  const [query, setQuery] = useState('');

  const handleSearch = (e) => {
    const searchQuery = e.target.value;
    setQuery(searchQuery);
    const filteredData = data.filter((item) =>
      item.name.toLowerCase().includes(searchQuery.toLowerCase())
    );
    onSearchResult(filteredData);
  };

  return (
    <div className="global-search-bar">
      <input
        type="text"
        placeholder="Search..."
        value={query}
        onChange={handleSearch}
      />
    </div>
  );
};

export default GlobalSearchBar;
