import { useState } from "react";

const SearchInput = ({ onSearch }) => {
  const [query, setQuery] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (query.trim()) {
      onSearch(query);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={query}
        placeholder="Ask a question to reach right person?"
        onChange={(e) => setQuery(e.target.value)}
        className="input"
      />
      <button className="button" type="submit">Search</button>
    </form>
  );
};

export default SearchInput;
