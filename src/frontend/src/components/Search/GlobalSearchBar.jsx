import React, { useState } from "react";

const GlobalSearchBar = () => {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    try {
      const res = await fetch(`/api/search?query=${query}`);
      const data = await res.json();
      setResults(data.results);
    } catch (err) {
      console.error("Search error:", err);
    }
  };

  return (
    <div className="global-search-bar">
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search..."
      />
      <button onClick={handleSearch}>Search</button>
      <div className="search-results">
        {results.map((item, idx) => (
          <div key={idx} className="search-item">
            {item.name}
          </div>
        ))}
      </div>
    </div>
  );
};

export default GlobalSearchBar;
