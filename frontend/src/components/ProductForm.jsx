import { useState, useEffect } from 'react';

export default function ProductForm({ categories, initial, onSubmit }) {
  const [form, setForm] = useState(
    initial ?? { name: '', price: '', category_id: categories?.[0]?.id ?? '' }
  );

  useEffect(() => {
    if (initial) setForm(initial);
  }, [initial]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm((f) => ({ ...f, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(form);
  };

  return (
    <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '0.8rem' }}>
      <input
        placeholder="Name"
        name="name"
        value={form.name}
        onChange={handleChange}
        required
      />
      <input
        placeholder="Price"
        name="price"
        type="number"
        step="0.01"
        value={form.price}
        onChange={handleChange}
        required
      />
      <select name="category_id" value={form.category_id} onChange={handleChange} required>
        {categories.map((c) => (
          <option key={c.id} value={c.id}>
            {c.name}
          </option>
        ))}
      </select>
      <button type="submit" style={{ padding: '0.4rem 1rem' }}>
        Save
      </button>
    </form>
  );
}