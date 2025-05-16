import React, { useState } from 'react';

const DataCard = ({item:data}) => {
  // State to control visibility of extra info
  const [showMore, setShowMore] = useState(false);


  // Function to toggle the 'Show More' button
  const toggleMoreInfo = () => {
    setShowMore(!showMore);
  };

    const mainFields =['Alias','name','CI ID','Service Owner','Service Team',
        'Service Executive ','Short Description'];
    const excludeFields = ["Text","n_tokens","index"];    
  return (
    <div className="data-card" style={styles.card}>
     {data.Name && <p><strong>Name:</strong> {data.Name}{data.Alias ? `(${data.Alias}` : ""}</p>}
     {data['Short Description'] && <p><strong>Short Description:</strong> {data['Short Description'] || ''}</p>}
     {data['Service Executive '] && <p><strong>Service Executive:</strong> {data['Service Executive '] || ''}</p>}
      <p><strong>Service Team:</strong> {data['Service Team'] || ''}</p>
      {showMore && ( 
                <div className="extra-info" style={styles.extraInfo}>
        {Object.entries(data).map(([key,value]) => {
            if([...mainFields,...excludeFields].includes(key)) return null
            return (value && <p><strong>{key} : </strong> {data[key]}</p>);
        })}
        
        </div>
      )}
      <button
        onClick={toggleMoreInfo}
        style={styles.button}
      >
        {showMore ? 'Show Less' : 'Show More'}
      </button>
    </div>
  );
};

const styles = {
  card: {
    padding: '20px',
    backgroundColor: '#f9f9f9',
    borderRadius: '8px',
    width: '100%',
    boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
    marginBottom: '20px',
  },
  extraInfo: {
    marginTop: '10px',
    fontSize: '14px',
    color: '#555',
  },
  button: {
    marginTop: '10px',
    backgroundColor: '#007bff',
    color: 'white',
    border: 'none',
    padding: '5px 10px',
    cursor: 'pointer',
    fontSize: '14px',
    borderRadius: '5px',
  }
};

export default DataCard;
