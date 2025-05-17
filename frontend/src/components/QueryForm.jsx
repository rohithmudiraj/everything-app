import React, { useState } from "react";
import FloatingPillBubbles from "./FloatingPillBubbles.jsx";


export default function QueryForm({onSubmit}) {
  const [query, setQuery] = useState("");

  function handleSubmit(e) {
    e.preventDefault();
    onSubmit(query);
  }

  return (
    <>
      <form onSubmit={handleSubmit} className="row justify-content-center mb-2">
        <div className="col-md-6 mb-2">
          <input
            type="text"
            className="form-control form-control-lg"
            placeholder="Have a question or facing an issue? Type here..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />
        </div>
        <div className="col-md-auto">
          <button type="submit" className="btn btn-primary btn-lg w-100">
            Search
          </button>
        </div>
      </form>

      {/* Pills below your existing search form */}
      {/* <FloatingPillBubbles query={query} setQuery={setQuery} suggestions={suggestions} /> */}
    </>
  );
}
