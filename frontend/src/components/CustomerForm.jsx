import { useState, useEffect } from 'react';

/** Форма клиента: { first_name, last_name, email, phone } */
export default function CustomerForm({ initial, onSubmit }) {
  const blank = { first_name: '', last_name: '', email: '', phone: '' };
  const [form, setForm] = useState(initial ?? blank);

  useEffect(() => setForm(initial ?? blank), [initial]);

  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });
  const handleSubmit = (e) => { e.preventDefault(); onSubmit(form); };

  return (
    <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '0.8rem' }}>
      <input name="first_name" placeholder="First name" value={form.first_name} onChange={handleChange} required />
      <input name="last_name" placeholder="Last name" value={form.last_name} onChange={handleChange} required />
      <input type="email" name="email" placeholder="Email" value={form.email} onChange={handleChange} required />
      <input name="phone" placeholder="Phone" value={form.phone} onChange={handleChange} required />
      <button type="submit" style={{ padding: '0.4rem 1rem' }}>Save</button>
    </form>
  );
}