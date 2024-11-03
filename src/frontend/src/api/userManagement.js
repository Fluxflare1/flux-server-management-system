// src/frontend/src/api/userManagement.js
import axiosInstance from "./axiosInstance";

export const createUser = (data) => axiosInstance.post("/users/", data);
export const updateUser = (userId, data) => axiosInstance.put(`/users/${userId}/`, data);
export const deleteUser = (userId) => axiosInstance.delete(`/users/${userId}/`);
export const fetchUsers = () => axiosInstance.get("/users/");
