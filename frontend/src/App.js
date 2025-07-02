import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import SupplierList from "./components/SupplierList";
import SupplierDetail from "./components/SupplierDetail";
import ComplianceForm from "./components/ComplianceForm";
import Insights from "./components/Insights";  // Remove this import

import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <h1>Supplier Dashboard</h1>

        {/* Navigation Links */}
        <nav>
          <Link to="/">Suppliers</Link>
          <Link to="/supplier/upload">Upload Compliance Data</Link>
          <Link to="/suppliers/insights">Insights</Link>
          

        </nav>

        {/* Routes */}
        <Routes>
          <Route path="/" element={<SupplierList />} />
          <Route path="/supplier/:id" element={<SupplierDetail />} />
          <Route path="/supplier/upload" element={<ComplianceForm />} />
           <Route path="/suppliers/insights" element={<Insights />} />

        </Routes>
      </div>
    </Router>
  );
}

export default App;
