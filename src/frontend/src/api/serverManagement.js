// src/frontend/src/api/serverManagement.js
import axiosInstance from "./axiosInstance";

export const createServer = (data) => axiosInstance.post("/server/create/", data);
export const startServer = (serverId) => axiosInstance.post(`/server/${serverId}/start/`);
export const stopServer = (serverId) => axiosInstance.post(`/server/${serverId}/stop/`);
export const deleteServer = (serverId) => axiosInstance.delete(`/server/${serverId}/delete/`);
