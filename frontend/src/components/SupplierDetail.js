import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const SupplierDetail = () => {
  const { id } = useParams();
  const [supplier, setSupplier] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get(`http://127.0.0.1:8000/suppliers/${id}`)
      .then(res => setSupplier(res.data))
      .catch(() => setError("Failed to load supplier details."));
  }, [id]);

  if (error) return <p>{error}</p>;
  if (!supplier) return <p>Loading...</p>;

  return (
    <div>
      <h2>{supplier.name} (ID: {supplier.id})</h2>
      <p><strong>Country:</strong> {supplier.country}</p>
      <p><strong>Compliance Score:</strong> {supplier.compliance_score ?? "N/A"}</p>
      <p><strong>Last Audit:</strong> {supplier.last_audit ?? "N/A"}</p>

      <h3>Contract Terms:</h3>
      <ul>
        {supplier.contract_terms && Object.entries(supplier.contract_terms).map(([key, value]) => (
          <li key={key}><strong>{key}:</strong> {value}</li>
        ))}
      </ul>

      <h3>Compliance Records:</h3>
      {supplier.compliance_records && supplier.compliance_records.length === 0 ? (
        <p>No records available</p>
      ) : (
        <ul>
          {supplier.compliance_records.map(record => (
            <li key={record.id}>
              <strong>{record.metric}</strong> on {record.date_recorded} - {record.result} ({record.status})
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default SupplierDetail;
