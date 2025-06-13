import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Home from './pages/Home';
import Notifications from './pages/Notifications';

export default function App() {
  return (
    <BrowserRouter>
      <nav className="p-4 bg-washu text-white flex space-x-4">
        <Link to="/">Home</Link>
        <Link to="/notifications">Notificações</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/notifications" element={<Notifications />} />
      </Routes>
    </BrowserRouter>
  );
}
