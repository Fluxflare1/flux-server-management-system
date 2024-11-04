// src/frontend/src/components/ActivityLog/ActivityLogFilter.js
import React, { useState } from 'react';

const ActivityLogFilter = ({ setFilter }) => {
    const [user, setUser] = useState('');
    const [action, setAction] = useState('');
    const [date, setDate] = useState('');

    const applyFilter = () => {
        setFilter({ user, action, date });
    };

    return (
        <div>
            <input
                type="text"
                placeholder="User"
                value={user}
                onChange={(e) => setUser(e.target.value)}
            />
            <input
                type="text"
                placeholder="Action"
                value={action}
                onChange={(e) => setAction(e.target.value)}
            />
            <input
                type="date"
                value={date}
                onChange={(e) => setDate(e.target.value)}
            />
            <button onClick={applyFilter}>Apply Filter</button>
        </div>
    );
};

export default ActivityLogFilter;
