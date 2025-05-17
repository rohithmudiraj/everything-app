import React from "react";

export default function FloatingPillBubbles({ query, setQuery, suggestions }) {
  // Filter suggestions based on query (optional, or you can pre-filter outside)
  const filtered = suggestions.filter((s) =>
    s.toLowerCase().includes(query.toLowerCase())
  );

  function handleClick(suggestion) {
    setQuery(suggestion);
  }

//   if (!query || filtered.length === 0) return null;

  return (
    <div className="d-flex flex-wrap gap-2 mt-5" style={{ maxWidth: "800px", margin: "0 auto" }}>
      {filtered.map((s, i) => (
        <div
          key={i}
          onMouseDown={() => handleClick(s)} // use onMouseDown to avoid losing focus before click
          className="pill-bubble"
          title="Click to select"
          style={{
            backgroundColor: "#0d6efd",
            color: "white",
            padding: "6px 14px",
            borderRadius: "20px",
            fontSize: "0.85rem",
            cursor: "pointer",
            userSelect: "none",
            transition: "background-color 0.2s ease",
          }}
          onMouseEnter={(e) => (e.currentTarget.style.backgroundColor = "#084298")}
          onMouseLeave={(e) => (e.currentTarget.style.backgroundColor = "#0d6efd")}
        >
          {s}
        </div>
      ))}
    </div>
  );
}
