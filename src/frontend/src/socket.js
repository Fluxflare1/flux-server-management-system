import { io } from "socket.io-client";

const socket = io("http://<backend-url>");

socket.on("connect", () => {
  console.log("Connected to server");
});

socket.on("update", (data) => {
  console.log("Update received:", data);
});

export default socket;
