// Path: frontend/src/pages/Dashboard.js
import React, { useState } from 'react';
import GlobalSearchBar from '../components/Search/GlobalSearchBar';

const Dashboard = ({ resources }) => {
  const [searchResults, setSearchResults] = useState([]);

  return (
    <div>
      <GlobalSearchBar data={resources} onSearchResult={setSearchResults} />
      <ul>
        {searchResults.map((result, index) => (
          <li key={index}>{result.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default Dashboard;
