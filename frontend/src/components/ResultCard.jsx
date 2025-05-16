import React from 'react';
const ResultCard = ({ item:data }) => {
  // Fields to exclude from display
  const excludedFields = ['Text', 'n_tokens', 'index'];

  // Function to render a field only if it has a value
  const renderField = (label, value) => {
    if (value && !excludedFields.includes(label)) {
      return (
        <div className="field" key={label}>
          <strong>{label}:</strong> {value}
        </div>
      );
    }
    return null;
  };

  return (
    <div className="search-card">
      {data && Object.entries(data).map(([key, value]) => renderField(key, value))}
    </div>
  );
};

export default ResultCard;

