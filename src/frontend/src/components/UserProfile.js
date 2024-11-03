// src/frontend/src/components/UserProfile.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function UserProfile() {
    const [profile, setProfile] = useState({});

    useEffect(() => {
        axios.get('/api/profile')
            .then(response => setProfile(response.data))
            .catch(error => console.error(error));
    }, []);

    const handleUpdate = () => {
        axios.put('/api/profile', profile)
            .then(response => alert('Profile updated'))
            .catch(error => console.error(error));
    };

    return (
        <div>
            <h2>User Profile</h2>
            <input
                type="text"
                value={profile.name}
                onChange={e => setProfile({ ...profile, name: e.target.value })}
            />
            <button onClick={handleUpdate}>Update Profile</button>
        </div>
    );
}

export default UserProfile;
