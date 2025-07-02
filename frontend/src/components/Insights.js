import React, { useEffect, useState } from "react";
import api from "../api";
import ReactMarkdown from "react-markdown";

export default function Insights() {
  const [insights, setInsights] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    api.get("/suppliers/insights")
      .then(res => {
        if (res.data.insights) {
          setInsights(res.data.insights);
        } else {
          setInsights(JSON.stringify(res.data));  // fallback
        }
        setLoading(false);
      })
      .catch(() => {
        setError("Failed to load insights");
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading insights...</p>;
  if (error) return <p style={{ color: "red" }}>{error}</p>;

  return (
    <div>
      <h2>AI-Powered Compliance Insights</h2>
      <ReactMarkdown>{insights}</ReactMarkdown>
    </div>
  );
}
