// Path: frontend/src/components/CustomerDashboard/Notifications.js
import React, { useState, useEffect } from 'react';

const Notifications = ({ notifications }) => {
  const [unread, setUnread] = useState(notifications.filter(n => !n.read));

  useEffect(() => {
    const interval = setInterval(() => {
      // Simulating incoming notifications
      const newNotification = {
        id: unread.length + 1,
        message: `Server load exceeds threshold!`,
        timestamp: new Date().toLocaleTimeString(),
        read: false,
      };
      setUnread([...unread, newNotification]);
    }, 10000); // Mock notification every 10 seconds

    return () => clearInterval(interval);
  }, [unread]);

  const markAsRead = (id) => {
    setUnread(unread.map(n => (n.id === id ? { ...n, read: true } : n)));
  };

  return (
    <div>
      <h3>Notifications</h3>
      <ul>
        {unread.map((notification) => (
          <li key={notification.id}>
            <p>{notification.message}</p>
            <small>{notification.timestamp}</small>
            {!notification.read && (
              <button onClick={() => markAsRead(notification.id)}>Mark as Read</button>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Notifications;
