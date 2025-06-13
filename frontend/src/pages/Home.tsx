import { useState, useEffect } from 'react';

interface Car {
  id: number;
  model: string;
  plate: string;
}

export default function Home() {
  const [cars, setCars] = useState<Car[]>([]);
  const [model, setModel] = useState('');
  const [plate, setPlate] = useState('');

  useEffect(() => {
    fetch('http://localhost:8000/cars/')
      .then(res => res.json())
      .then(setCars);
  }, []);

  const addCar = async () => {
    await fetch('http://localhost:8000/cars/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ model, plate })
    });
    setModel('');
    setPlate('');
    const updated = await fetch('http://localhost:8000/cars/').then(r => r.json());
    setCars(updated);
  };

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold text-pink-700 mb-4">🚗 Carros Disponíveis</h1>
      <div className="mb-6 space-x-2">
        <input
          value={model}
          onChange={e => setModel(e.target.value)}
          placeholder="Modelo"
          className="p-2 border rounded"
        />
        <input
          value={plate}
          onChange={e => setPlate(e.target.value)}
          placeholder="Placa"
          className="p-2 border rounded"
        />
        <button
          onClick={addCar}
          className="px-4 py-2 bg-pink-500 text-white rounded"
        >
          Adicionar
        </button>
      </div>
      <ul className="space-y-2">
        {cars.map(car => (
          <li
            key={car.id}
            className="p-4 bg-white rounded shadow flex items-center justify-between"
          >
            <div>
              <strong>{car.model}</strong> — {car.plate}
            </div>
            <button
              onClick={async () => {
                await fetch(`http://localhost:8000/cars/${car.id}`, { method: 'DELETE' });
                setCars(cars.filter(c => c.id !== car.id));
              }}
              className="px-2 py-1 bg-red-500 text-white rounded hover:bg-red-600 transition"
            >
              Remover
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
