// src/services/apiService.js

import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000/api/v1';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: { 'Content-Type': 'application/json' },
});

// Interceptor for handling token expiration
apiClient.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response?.status === 401 && error.config && !error.config._retry) {
      error.config._retry = true;
      try {
        const refreshToken = localStorage.getItem('refresh_token');
        const { data } = await axios.post(`${API_BASE_URL}/auth/refresh/`, { refresh: refreshToken });
        localStorage.setItem('access_token', data.access);
        apiClient.defaults.headers.common['Authorization'] = `Bearer ${data.access}`;
        return apiClient(error.config);
      } catch (e) {
        console.error('Token refresh failed:', e);
        window.location.href = '/login';
      }
    }
    return Promise.reject(error);
  }
);

// Authentication APIs
export const login = (credentials) => apiClient.post('/auth/login/', credentials);
export const register = (userData) => apiClient.post('/auth/register/', userData);

// User APIs
export const fetchUserDetails = () => apiClient.get('/user/profile/', {
  headers: { Authorization: `Bearer ${localStorage.getItem('access_token')}` },
});

// Server Management APIs
export const getServerList = () => apiClient.get('/servers/', {
  headers: { Authorization: `Bearer ${localStorage.getItem('access_token')}` },
});

export const getBillingDetails = () => apiClient.get('/billing/', {
  headers: { Authorization: `Bearer ${localStorage.getItem('access_token')}` },
});
