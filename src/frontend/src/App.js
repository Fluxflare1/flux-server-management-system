



// src/frontend/src/App.js

import Payment from "./components/Payments/Payment";

function App() {
    return (
        <div className="App">
            {/* Other routes */}
            <Route path="/payment" component={Payment} />
        </div>
    );
}

export default App;




import React, { useEffect, useState } from 'react';

function App() {
    const [message, setMessage] = useState('');

    useEffect(() => {
        fetch('/')
            .then((res) => res.json())
            .then((data) => setMessage(data.message))
            .catch((err) => console.error(err));
    }, []);

    return (
        <div>
            <h1>Flux Server Management System</h1>
            <p>{message}</p>
        </div>
    );
}

export default App;
