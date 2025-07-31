import { Link, Route, Routes, NavLink } from 'react-router-dom';
import ProductsPage from './pages/ProductsPage';
import CategoriesPage from './pages/CategoriesPage';
import CustomersPage from './pages/CustomersPage';

const navStyle = {
  padding: '1rem',
  gap: '1rem',
  display: 'flex',
  borderBottom: '1px solid #ccc',
};

export default function App() {
  return (
    <>
      <nav style={navStyle}>
        <NavLink to="/products">Products</NavLink>
        <NavLink to="/categories">Categories</NavLink>
        <NavLink to="/customers">Customers</NavLink>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/products" element={<ProductsPage />} />
        <Route path="/categories" element={<CategoriesPage />} />
        <Route path="/customers" element={<CustomersPage />} />
      </Routes>
    </>
  );
}

function Home() {
  return (
    <div style={{ padding: '2rem' }}>
      <h2>ERP Dashboard</h2>
      <p>Select a module from the navigation.</p>
    </div>
  );
}