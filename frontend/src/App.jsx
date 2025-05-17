import { useState } from 'react';
import QueryForm from './components/QueryForm.jsx';
import ContactList from './components/ContactList.jsx';
import { queryData } from './api/search.jsx';

export default function App() {

  const [contacts, setContacts] = useState([]);
  const [loading, setLoading] = useState(false);
  const [searched,setSearched] = useState(false);
  const handleSearch = async (query) => {
      setLoading(true);
      try {
        const res = await queryData(query);
        setContacts(res);
        setSearched(true);
      } catch (err) {
        console.error("Error querying data:", err);
      }
      setLoading(false);
    };

    const loader =()=> {
      return(<div class="text-center">
  <div class="spinner-border" role="status">
    <span class="visually-hidden">Loading...</span>
  </div>
</div>);
    }

  return (
    // <div className='bg-primary bg-gradient rounded-3 shadow-lg p-4 mb-4 text-white'>
     <div className="container py-5">
      <h1 className="display-4 text-center  mb-4 mr-4">SmartHelp: Ask & Connect</h1>
      <QueryForm onSubmit={handleSearch} />
      <ContactList contacts={contacts} searched={searched} />
      {loading && loader()}
    </div>
  );
}
