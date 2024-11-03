// src/frontend/src/api/resourceMonitoring.js
import axiosInstance from "./axiosInstance";

export const fetchMetrics = () => axiosInstance.get("/metrics/");
