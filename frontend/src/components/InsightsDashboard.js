import React, { useEffect, useState } from "react";
import api from "../api";

export default function Insights() {
  const [insights, setInsights] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    api.get("/suppliers/insights")
      .then(res => {
        setInsights(res.data.insights || res.data); // adjust based on your backend response
        setLoading(false);
      })
      .catch(() => {
        setError("Failed to load insights");
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Loading insights...</div>;
  if (error) return <div style={{ color: "red" }}>{error}</div>;

  return (
    <div>
      <h2>AI-Powered Compliance Insights</h2>
      <p style={{ whiteSpace: "pre-wrap" }}>{insights}</p>
    </div>
  );
}
