import numpy as np
import os
from app.data_loader import load_data
from app.search import SemanticSearch
from utils import generate_embeddings_safely, save_embeddings

# Initialize the search_engine
def initialize_search_engine(fromcache=True):
    data_file_path = "data/stake_holder_data.xlsx"
    if not os.path.exists(data_file_path):
        raise FileNotFoundError(f"Data file not found: {data_file_path}")
    df = load_data(data_file_path)
    # if os.path.exists("embeddings.npy") and fromcache:
    #     embeddings= np.load("embeddings.npy")
    # else:    
    embeddings = generate_embeddings_safely(df["Text"].tolist(), "search_document")
    embeddings = np.array(embeddings)
    save_embeddings("embeddings.npy", embeddings)
    global search_engine
    search_engine= SemanticSearch(df, embeddings)
    return search_engine

# Shared function to get the search engine instance
search_engine = None  # This will be set at app startup

def get_search_engine():
    global search_engine
    if search_engine is None:
        raise Exception("Search engine is not initialized yet!")
    return search_engine
