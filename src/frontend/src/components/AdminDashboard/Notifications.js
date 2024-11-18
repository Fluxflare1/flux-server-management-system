// Path: frontend/src/components/AdminDashboard/Notifications.js
import React, { useState, useEffect } from 'react';

const Notifications = () => {
  const [notifications, setNotifications] = useState([]);

  useEffect(() => {
    // Simulated API call to fetch notifications
    const fetchNotifications = async () => {
      const response = [
        { id: 1, message: 'Server load increased by 20%', type: 'warning' },
        { id: 2, message: 'New user registered: John Doe', type: 'info' },
      ];
      setNotifications(response);
    };

    fetchNotifications();
  }, []);

  return (
    <div>
      <h3>Notifications</h3>
      <ul>
        {notifications.map((notification) => (
          <li key={notification.id} className={`notification ${notification.type}`}>
            {notification.message}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Notifications;
