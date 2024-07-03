// twix-ai-frontend/src/utils/api.ts
import axios from 'axios';

const API_URL = 'http://localhost:5000'; // Replace with your Flask backend URL

const api = axios.create({
    baseURL: API_URL,
    timeout: 10000,
});

export default api;
