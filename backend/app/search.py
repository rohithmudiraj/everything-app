import faiss
import numpy as np

#responsible for indexing data to fiass db and querying it
class SemanticSearch:
    def __init__(self, df, embeddings):
        self.df = df
        self.index = faiss.IndexFlatL2(len(embeddings[0]))
        self.index.add(np.array(embeddings).astype("float32"))
        # Save the FAISS index to disk for later use
        faiss.write_index(self.index, "data/faiss_index.index")
        # Optionally, save the corresponding DataFrame indices for reference (e.g., to retrieve full rows later)
        df['index'] = df.index  # Add the original DataFrame index as a column
        df.to_csv("data/data_with_index.csv", index=False)

    def query(self, text_embedding, top_k=3):
        D, I = self.index.search(np.array([text_embedding]).astype("float32"), top_k)
        return self.df.iloc[I[0]]
