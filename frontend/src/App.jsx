import React from 'react'
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { useEffect } from 'react'
import Login from "./pages/Login.jsx"
import Register from "./pages/Register.jsx"
import Home from "./pages/Home.jsx"
import NotFound from "./pages/NotFound.jsx"
import ProtectedRoute from './components/ProtectedRoute.jsx'
import { ACCESS_TOKEN, REFRESH_TOKEN } from './constants.js'

function Logout() {
  useEffect(() => {
    localStorage.removeItem(ACCESS_TOKEN);
    localStorage.removeItem(REFRESH_TOKEN);
  }, []);
  return <Navigate to="/login" />;
}

function RegisterAndLogout() {
  useEffect(() => {
    localStorage.removeItem(ACCESS_TOKEN);
    localStorage.removeItem(REFRESH_TOKEN);
  }, []);
  return <Register />
}


function App() {

  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/"
          element={
            <ProtectedRoute>
              <Home />
            </ProtectedRoute>
          }
        />
        <Route path="/login" element={<Login />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="/register" element={<RegisterAndLogout />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
