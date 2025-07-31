import { useEffect, useState } from 'react';
import UniversalTable from '../components/UniversalTable';
import Modal from '../components/Modal';
import CategoryForm from '../components/CategoryForm';
import Toast from '../components/Toast';
import { fetchTable, addItem, deleteItem } from '../api/http';

export default function CategoriesPage() {
  const [table, setTable] = useState(null);
  const [toast, setToast] = useState(null);
  const [open, setOpen] = useState(false);

  const showErr = (e)=>setToast(e?.response?.data?.detail ?? e.message);
  const load = ()=>fetchTable('/category').then(setTable).catch(showErr);
  useEffect(()=>{load();},[]);

  const submit = (v)=>addItem('/category', v).then(()=>{setOpen(false); load();}).catch(showErr);
  const del = (r)=>{ if(confirm('Delete?')) deleteItem('/category', r.id).then(load).catch(showErr);} ;

  return (
    <div style={{ padding: '2rem' }}>
      <h2>Categories</h2>
      <button onClick={()=>setOpen(true)} style={{ padding:'0.4rem 0.8rem' }}>+ Add Category</button>
      {table ? <UniversalTable tableData={table} onDelete={del} /> : <p>Loading…</p>}
      <Modal isOpen={open} onClose={()=>setOpen(false)} title="Add Category">
        <CategoryForm onSubmit={submit} />
      </Modal>
      <Toast message={toast} onClear={() => setToast(null)} />
    </div>
  );
}