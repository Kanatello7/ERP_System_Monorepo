import { useEffect } from 'react';

/**
 * Простое всплывающее окно (toast).
 * message – строка или null; исчезает через `duration` мс.
 */
export default function Toast({ message, onClear, duration = 5000 }) {
  useEffect(() => {
    if (!message) return;
    const t = setTimeout(onClear, duration);
    return () => clearTimeout(t);
  }, [message, onClear, duration]);

  if (!message) return null;

  return (
    <div style={style}>
      {message}
    </div>
  );
}

const style = {
  position: 'fixed',
  bottom: '1rem',
  right: '1rem',
  background: '#f87171', // красный
  color: '#fff',
  padding: '0.75rem 1rem',
  borderRadius: '4px',
  boxShadow: '0 2px 8px rgba(0,0,0,0.15)',
  zIndex: 100,
};