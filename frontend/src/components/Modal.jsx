export default function Modal({ isOpen, onClose, title, children }) {
  if (!isOpen) return null;
  return (
    <div style={backdrop}>
      <div style={modalBox}>
        <h3>{title}</h3>
        {children}
        <button style={closeBtn} onClick={onClose}>Close</button>
      </div>
    </div>
  );
}

const backdrop = {
  position: 'fixed',
  inset: 0,
  background: 'rgba(0,0,0,0.4)',
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center',
  zIndex: 50,
};
const modalBox = {
  background: '#fff',
  padding: '1.5rem',
  borderRadius: '8px',
  minWidth: '320px',
  maxWidth: '90%',
};
const closeBtn = {
  marginTop: '1rem',
  padding: '0.3rem 0.8rem',
};