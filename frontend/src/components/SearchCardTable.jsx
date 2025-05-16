import React from 'react';

const SearchCardTable = ({ dataList }) => {
    console.log(dataList);
    const columnKeys=Object.keys(dataList[0]);
    console.log(columnKeys);
  // Fields to exclude from display
  const excludedFields = ['Text', 'n_tokens', 'index'];

  // Function to render a row only if it has a value
  const renderRow = (label, value) => {
    if (value && !excludedFields.includes(label)) {
      return (
        <td key={label}>
          {value}
        </td>
      );
    }
    return null;
  };

  return (
    <div className="search-card-table">
      <table>
        <thead>
          <tr>
            {columnKeys.map(column=><th>{column}</th>)}
          </tr>
        </thead>
        <tbody>
          {dataList.map((data, index) => (
            <tr key={index}>
              {Object.entries(data).map(([key, value]) => renderRow(key, value))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default SearchCardTable;
