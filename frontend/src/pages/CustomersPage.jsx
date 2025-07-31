import { useEffect, useState } from 'react';
import UniversalTable from '../components/UniversalTable';
import Modal from '../components/Modal';
import CustomerForm from '../components/CustomerForm';
import Toast from '../components/Toast';
import { fetchTable, addItem, updateItem, deleteItem } from '../api/http';

export default function CustomersPage() {
  const [table, setTable] = useState(null);
  const [toast, setToast] = useState(null);
  const [open, setOpen] = useState(false);
  const [editing, setEditing] = useState(null);

  const showErr = (e)=>setToast(e?.response?.data?.detail ?? e.message);
  const load = ()=>fetchTable('/customers').then(setTable).catch(showErr);
  useEffect(()=>{load();},[]);

  const submit = (v)=>{
    const fn = editing ? updateItem('/customers', editing.id, v) : addItem('/customers', v);
    fn.then(()=>{setOpen(false); load();}).catch(showErr);
  };
  const del = (r)=>{ if(confirm('Delete?')) deleteItem('/customers', r.id).then(load).catch(showErr);} ;

  return (
    <div style={{ padding: '2rem' }}>
      <h2>Customers</h2>
      <button onClick={()=>{setEditing(null);setOpen(true);}} style={{padding:'0.4rem 0.8rem'}}>+ Add Customer</button>
      {table ? <UniversalTable tableData={table} onEdit={(r)=>{setEditing(r);setOpen(true);}} onDelete={del} /> : <p>Loading…</p>}
      <Modal isOpen={open} onClose={()=>setOpen(false)} title={editing? 'Edit Customer':'Add Customer'}>
        <CustomerForm initial={editing} onSubmit={submit} />
      </Modal>
      <Toast message={toast} onClear={() => setToast(null)} />
    </div>
  );
}