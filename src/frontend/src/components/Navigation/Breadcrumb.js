

const breadcrumbPaths = [
  { label: 'Dashboard', url: '/' },
  {
    label: 'Servers',
    url: '/servers',
    subItems: [
      { label: 'Active Servers', url: '/servers/active' },
      { label: 'Archived Servers', url: '/servers/archived' },
    ],
  },
  { label: 'Server Details', url: '/servers/123' },
];
<Breadcrumb paths={breadcrumbPaths} />;




// Path: frontend/src/components/Navigation/Breadcrumb.js
import React from 'react';
import { Link } from 'react-router-dom';

const Breadcrumb = ({ paths }) => {
  return (
    <nav className="breadcrumb">
      {paths.map((path, index) => (
        <span key={index} className="breadcrumb-item">
          <Link to={path.url}>{path.label}</Link>
          {path.subItems && (
            <div className="dropdown">
              {path.subItems.map((subItem, subIndex) => (
                <Link key={subIndex} to={subItem.url}>
                  {subItem.label}
                </Link>
              ))}
            </div>
          )}
          {index < paths.length - 1 && ' > '}
        </span>
      ))}
    </nav>
  );
};

export default Breadcrumb;



// Path: frontend/src/components/Navigation/Breadcrumb.js
import React from 'react';
import { Link } from 'react-router-dom';

const Breadcrumb = ({ paths }) => {
  return (
    <nav className="breadcrumb">
      {paths.map((path, index) => (
        <span key={index}>
          <Link to={path.url}>{path.label}</Link>
          {index < paths.length - 1 && ' > '}
        </span>
      ))}
    </nav>
  );
};

export default Breadcrumb;
