import axios from 'axios';

// base URLs из .env или дефолты
const PRODUCTS_URL  = import.meta.env.VITE_PRODUCTS_URL  || 'http://localhost:8002';
const CUSTOMERS_URL = import.meta.env.VITE_CUSTOMERS_URL || 'http://localhost:8001';

// определяем, к какому сервису пойдём по первому сегменту пути
const pickBase = (endpoint) => {
  if (endpoint.startsWith('/products') || endpoint.startsWith('/category')) return PRODUCTS_URL;
  if (endpoint.startsWith('/customers')) return CUSTOMERS_URL;
  return PRODUCTS_URL;
};

const request = (method, endpoint, body) =>
  axios({ method, url: pickBase(endpoint) + endpoint, data: body });

export const fetchTable = (endpoint) => request('get', `${endpoint}/table`).then((r) => r.data);
export const listItems  = (endpoint) => request('get', endpoint).then((r) => r.data);
export const addItem    = (endpoint, payload) => request('post', endpoint, payload).then((r) => r.data);
export const updateItem = (endpoint, id, payload) => request('put', `${endpoint}/${id}`, payload).then((r) => r.data);
export const deleteItem = (endpoint, id) => request('delete', `${endpoint}/${id}`);