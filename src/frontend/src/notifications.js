const userId = localStorage.getItem("userId"); // Example user ID storage
const socket = new WebSocket(`ws://localhost:8000/ws/notifications/`);

socket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    alert(`${data.title}: ${data.message}`);
};

socket.onopen = () => {
    console.log("WebSocket connection established.");
};

socket.onclose = () => {
    console.log("WebSocket connection closed.");
};
