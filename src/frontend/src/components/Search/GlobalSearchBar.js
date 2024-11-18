


// Path: frontend/src/components/Search/GlobalSearchBar.js
import React, { useState } from 'react';
import Fuse from 'fuse.js';

const GlobalSearchBar = ({ data, onSearchResult }) => {
  const [query, setQuery] = useState('');
  const fuse = new Fuse(data, { keys: ['name', 'type'], threshold: 0.3 });

  const handleSearch = (e) => {
    setQuery(e.target.value);
    const results = fuse.search(e.target.value).map((result) => result.item);
    onSearchResult(results);
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
