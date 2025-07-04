import React from "react";
import { Routes, Route } from "react-router-dom";
import Layout from "./layouts/Layout";

import Dashboard from "./pages/Dashboard";
import Detection from "./pages/Detection";
import Reports from "./pages/Reports";
import Settings from "./pages/Settings";
import Home from "./pages/Home";
import Streaming from "./pages/Streaming";
import { AuthProvider } from "./context/AuthContext";


const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route path="Home" element={<Home />} />
        <Route path="Streaming" element={<Streaming />} />              
        <Route path="dashboard" element={<Dashboard />} />
        <Route path="detection" element={<Detection />} />
        <Route path="reports" element={<Reports />} />
        <Route path="settings" element={<Settings />} />
      </Route>
    </Routes>
  );
};

export default App;

