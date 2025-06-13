import { useState } from 'react';

interface RentalNotify {
  id: number;
  customer: string;
  due_date: string;
  days_left: number;
}

export default function Notifications() {
  const [list, setList] = useState<RentalNotify[]>([]);

  const loadNotifications = async () => {
    const res = await fetch('http://localhost:7071/api/NotifyDueRentals');
    const json = await res.json();
    setList(json.notify);
  };

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold text-purple-700 mb-4">🔔 Aluguéis Vencidos ou Próximos</h1>
      <button onClick={loadNotifications}
        className="px-4 py-2 bg-purple-500 text-white rounded mb-6">
        Carregar Notificações
      </button>
      <ul className="space-y-2">
        {list.map(r => (
          <li key={r.id} className="p-4 bg-white rounded shadow">
            <p><strong>ID:</strong> {r.id}</p>
            <p><strong>Cliente:</strong> {r.customer}</p>
            <p><strong>Venceu em:</strong> {r.due_date} ({r.days_left} dias)</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
