import numpy as np
import os
from app.data_loader import load_contacts_data,load_group_data
from app.search import SemanticSearch
from utils import generate_embeddings_safely, save_embeddings
import pandas as pd

# Initialize the search_engine
def initialize_search_engine(fromcache=True):
    contacts_file_path = "data/stake_holder_data.csv"
    groups_file_path = "data/sys_user_group.csv"
    contacts_df=load_contacts_data_and_create_embeddings(contacts_file_path)
    groups_df=load_groups_data_and_create_embeddings(groups_file_path)   
    contacts_df["source"] = "contact"
    groups_df["source"] = "group"
    combined_df = pd.concat([contacts_df, groups_df], ignore_index=True)
    combined_df = combined_df.replace([np.inf, -np.inf], np.nan)
    combined_df = combined_df.where(pd.notnull(combined_df), None)
    embeddings = generate_embeddings_safely(combined_df["Text"].tolist(), "search_document")
    embeddings = np.array(embeddings)
    save_embeddings("data/embeddings.npy", embeddings)
    global search_engine
    search_engine= SemanticSearch(combined_df, embeddings)
    return search_engine

# Shared function to get the search engine instance
search_engine = None  # This will be set at app startup

def get_search_engine():
    global search_engine
    if search_engine is None:
        raise Exception("Search engine is not initialized yet!")
    return search_engine


def load_contacts_data_and_create_embeddings(data_file_path):
     if not os.path.exists(data_file_path):
        raise FileNotFoundError(f"Data file not found: {data_file_path}")
     return load_contacts_data(data_file_path)

def load_groups_data_and_create_embeddings(data_file_path):
     if not os.path.exists(data_file_path):
        raise FileNotFoundError(f"Data file not found: {data_file_path}")
     return load_group_data(data_file_path)
