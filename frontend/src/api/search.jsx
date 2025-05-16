import axios from 'axios';

// const API_BASE = import.meta.env.VITE_API_BASE || "http://localhost:80/api";

export const queryData = async (query) => {
  const res = await axios.get(`/api/query/`, {
    params: {query}
  });
  return res.data;
};
