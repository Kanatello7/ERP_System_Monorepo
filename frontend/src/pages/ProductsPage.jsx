import { useEffect, useState } from 'react';
import UniversalTable from '../components/UniversalTable';
import Modal from '../components/Modal';
import ProductForm from '../components/ProductForm';
import Toast from '../components/Toast';
import { fetchTable, listItems, addItem, updateItem, deleteItem } from '../api/http';

export default function ProductsPage() {
  const [table, setTable] = useState(null);
  const [categories, setCategories] = useState([]);
  const [toast, setToast] = useState(null);
  const [open, setOpen] = useState(false);
  const [editing, setEditing] = useState(null);

  const showErr = (e) => setToast(e?.response?.data?.detail ?? e.message);
  const load = () => fetchTable('/products').then(setTable).catch(showErr);
  const loadCats = () => listItems('/category').then(setCategories).catch(showErr);

  useEffect(() => { load(); loadCats(); }, []);

  const handleSubmit = (v) => {
    const fn = editing ? updateItem('/products', editing.id, v) : addItem('/products', v);
    fn.then(() => { setOpen(false); load(); }).catch(showErr);
  };
  const handleDelete = (r) => {
    if (confirm('Delete?')) deleteItem('/products', r.id).then(load).catch(showErr);
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h2>Products</h2>
      <button onClick={() => { setEditing(null); setOpen(true); }} style={{ padding: '0.4rem 0.8rem' }}>+ Add Product</button>
      {table ? <UniversalTable tableData={table} onEdit={(r)=>{setEditing(r);setOpen(true);}} onDelete={handleDelete} /> : <p>Loading…</p>}
      <Modal isOpen={open} onClose={()=>setOpen(false)} title={editing? 'Edit Product':'Add Product'}>
        <ProductForm categories={categories} initial={editing} onSubmit={handleSubmit} />
      </Modal>
      <Toast message={toast} onClear={() => setToast(null)} />
    </div>
  );
}