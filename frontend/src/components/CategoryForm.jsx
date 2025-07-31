import { useState, useEffect } from 'react';

/** Простая форма с полем name */
export default function CategoryForm({ initial, onSubmit }) {
  const [name, setName] = useState(initial?.name ?? '');

  useEffect(() => {
    if (initial) setName(initial.name);
  }, [initial]);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ name });
  };

  return (
    <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '0.8rem' }}>
      <input
        placeholder="Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        required
      />
      <button type="submit" style={{ padding: '0.4rem 1rem' }}>
        Save
      </button>
    </form>
  );
}