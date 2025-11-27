import axios from 'axios';

// Create an instance of axios with the base URL
const api = axios.create({
  baseURL: "https://api-spaceweb.dovis.dev", // 외부 접속용 주소
});

// Export the Axios instance
export default api;