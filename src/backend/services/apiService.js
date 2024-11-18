// services/apiService.js

import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000/api/v1';

// Authentication APIs
export const login = async (credentials) => {
  return axios.post(`${API_BASE_URL}/auth/login/`, credentials);
};

export const register = async (userData) => {
  return axios.post(`${API_BASE_URL}/auth/register/`, userData);
};

// User Data APIs
export const fetchUserDetails = async () => {
  const token = localStorage.getItem('access_token');
  return axios.get(`${API_BASE_URL}/user/profile/`, {
    headers: { Authorization: `Bearer ${token}` },
  });
};

// Server Management APIs
export const getServerList = async () => {
  const token = localStorage.getItem('access_token');
  return axios.get(`${API_BASE_URL}/servers/`, {
    headers: { Authorization: `Bearer ${token}` },
  });
};

// Additional APIs for resource monitoring, billing, etc.
export const getBillingDetails = async () => {
  const token = localStorage.getItem('access_token');
  return axios.get(`${API_BASE_URL}/billing/`, {
    headers: { Authorization: `Bearer ${token}` },
  });
};
