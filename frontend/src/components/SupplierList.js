import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import api from "../api";

export default function SupplierList() {
  const [suppliers, setSuppliers] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    api.get("/suppliers")
      .then(res => setSuppliers(res.data))
      .catch(() => setError("Failed to load suppliers"));
  }, []);

  if (error) return <div>{error}</div>;

  return (
    <div>
      <h2>Supplier List</h2>
      <ul>
        {suppliers.map(s => (
          <li key={s.id}>
            <Link to={`/supplier/${s.id}`}>
              <strong>{s.name}</strong>
            </Link>{" "}
            - Compliance Score: {s.compliance_score ?? "N/A"}
          </li>
        ))}
      </ul>
    </div>
  );
}
