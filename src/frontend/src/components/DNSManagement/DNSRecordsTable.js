// Path: src/frontend/components/DNSManagement/DNSRecordsTable.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';

const DNSRecordsTable = ({ domainName }) => {
    const [records, setRecords] = useState([]);

    useEffect(() => {
        // Fetch DNS records for the domain
        axios.get(`/api/dns/records?domain=${domainName}`)
            .then(response => setRecords(response.data.records))
            .catch(error => console.error(error));
    }, [domainName]);

    return (
        <table>
            <thead>
                <tr>
                    <th>Type</th>
                    <th>Value</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {records.map(record => (
                    <tr key={record.id}>
                        <td>{record.type}</td>
                        <td>{record.value}</td>
                        <td>
                            <button onClick={() => handleEdit(record.id)}>Edit</button>
                            <button onClick={() => handleDelete(record.id)}>Delete</button>
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>
    );
};
