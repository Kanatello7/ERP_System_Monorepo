import { useMemo } from 'react';
import { useReactTable, flexRender, getCoreRowModel } from '@tanstack/react-table';

export default function UniversalTable({ tableData, onEdit, onDelete }) {
  const baseCols = tableData.columns.map((col) => ({
    accessorKey: col.key,
    header: col.title,
  }));

  const columns = useMemo(() => {
    if (!onEdit && !onDelete) return baseCols;
    return [
      ...baseCols,
      {
        id: 'actions',
        header: 'Actions',
        cell: ({ row }) => (
          <div style={{ display: 'flex', gap: '0.4rem' }}>
            {onEdit && (
              <button onClick={() => onEdit(row.original)} title="Edit">
                ✏️
              </button>
            )}
            {onDelete && (
              <button onClick={() => onDelete(row.original)} title="Delete">
                🗑️
              </button>
            )}
          </div>
        ),
      },
    ];
  }, [baseCols, onEdit, onDelete]);

  const data = useMemo(
    () => tableData.rows.map((row) => row.values ?? row),
    [tableData.rows]
  );

  const table = useReactTable({ data, columns, getCoreRowModel: getCoreRowModel() });

  if (!data.length) return <p>No data</p>;

  return (
    <table style={tableStyle}>
      <thead style={{ background: '#f3f4f6' }}>
        {table.getHeaderGroups().map((hg) => (
          <tr key={hg.id}>
            {hg.headers.map((header) => (
              <th key={header.id} style={thTd}>
                {flexRender(header.column.columnDef.header, header.getContext())}
              </th>
            ))}
          </tr>
        ))}
      </thead>
      <tbody>
        {table.getRowModel().rows.map((row, idx) => (
          <tr key={row.id} style={idx % 2 ? stripe : {}}>
            {row.getVisibleCells().map((cell) => (
              <td key={cell.id} style={thTd}>
                {flexRender(cell.column.columnDef.cell, cell.getContext())}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}

const tableStyle = {
  borderCollapse: 'collapse',
  width: '100%',
  marginTop: '1rem',
};
const thTd = {
  border: '1px solid #d1d5db',
  padding: '0.5rem',
  textAlign: 'left',
};
const stripe = { background: '#fafafa' };