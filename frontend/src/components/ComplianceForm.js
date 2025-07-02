import React, { useState } from "react";
import api from "../api";

export default function ComplianceForm() {
  const [formData, setFormData] = useState({
    supplier_id: "",
    metric: "",
    date_recorded: "",
    result: "",
    status: ""
  });
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  function handleChange(e) {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  }

  async function handleSubmit(e) {
    e.preventDefault();
    setMessage("");
    setError("");

    try {
      const response = await api.post("/suppliers/check-compliance", formData);
      setMessage(response.data.message + " Pattern: " + response.data.pattern_analysis);
      setFormData({
        supplier_id: "",
        metric: "",
        date_recorded: "",
        result: "",
        status: ""
      });
    } catch (err) {
      setError("Failed to submit compliance data.");
    }
  }

  return (
    <div>
      <h2>Upload Compliance Data</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="number"
          name="supplier_id"
          placeholder="Supplier ID"
          value={formData.supplier_id}
          onChange={handleChange}
          required
        /><br />
        <input
          type="text"
          name="metric"
          placeholder="Metric (e.g., delivery time)"
          value={formData.metric}
          onChange={handleChange}
          required
        /><br />
        <input
          type="date"
          name="date_recorded"
          value={formData.date_recorded}
          onChange={handleChange}
          required
        /><br />
        <input
          type="text"
          name="result"
          placeholder="Result"
          value={formData.result}
          onChange={handleChange}
          required
        /><br />
        <select
          name="status"
          value={formData.status}
          onChange={handleChange}
          required
        >
          <option value="">Select status</option>
          <option value="compliant">compliant</option>
          <option value="non-compliant">non-compliant</option>
        </select><br />
        <button type="submit">Submit</button>
      </form>
      {message && <p style={{ color: "green" }}>{message}</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
}
