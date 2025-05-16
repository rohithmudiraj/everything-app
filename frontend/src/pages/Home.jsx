import { useState } from "react";
import SearchInput from "../components/SearchInput";
import ResultCard from "../components/ResultCard";
import { queryData } from "../api/search";
import SearchCardTable from "../components/SearchCardTable";
import DataCard from "../components/DataCard";

const Home = () => {
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async (query) => {
    setLoading(true);
    try {
      const res = await queryData(query);
      setResults(res);
    } catch (err) {
      console.error("Error querying data:", err);
    }
    setLoading(false);
  };

  return (
    <div className="container">
      <h1>AskDirect</h1>
      <SearchInput onSearch={handleSearch} />
      {loading && <p>Loading...</p>}
      {/* {results?.length>0 && <SearchCardTable dataList={results}/>} */}
      {results.map((item, idx) => (
        <DataCard key={idx} item={item} />
      ))}
    </div>
  );
};

export default Home;
