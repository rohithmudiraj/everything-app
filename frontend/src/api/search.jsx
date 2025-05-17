import axios from 'axios';

export const queryData = async (query) => {
  const res = await axios.get(`/api/query/`, {
    params: {query}
  });
  return res.data;
};
