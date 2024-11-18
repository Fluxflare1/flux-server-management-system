// Path: frontend/src/components/AdminDashboard/ResourceSummary.js
import React from 'react';

const ResourceSummary = ({ resources }) => {
  return (
    <div>
      <h3>Resource Allocation Summary</h3>
      <table>
        <thead>
          <tr>
            <th>Client</th>
            <th>CPU</th>
            <th>Memory</th>
            <th>Storage</th>
          </tr>
        </thead>
        <tbody>
          {resources.map((resource, index) => (
            <tr key={index}>
              <td>{resource.client}</td>
              <td>{resource.cpu}%</td>
              <td>{resource.memory}GB</td>
              <td>{resource.storage}GB</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ResourceSummary;
