import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Control from './pages/control';
import Login from './pages/login';
function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Control />}></Route>
        <Route path="/control" element={<Login />}></Route>
      </Routes>
    </BrowserRouter>
  );
}
export default AppRoutes;
