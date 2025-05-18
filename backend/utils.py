import pandas as pd
import numpy as np
import faiss
import os
import requests
from dotenv import load_dotenv

load_dotenv()

TIP_AI_VIRTUAL_KEY = os.getenv("TIP_AI_VIRTUAL_KEY")
TIP_AI_URL=os.getenv("TIP_AI_URL")
MODEL=os.getenv("MODEL")

def generate_embeddings(text_data,input_type):
    embeddings = create_cohere_embeddings(text_data,input_type)
    return [embedding['embedding'] for embedding in embeddings['data']]

def create_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

def delete_files(folder_path):
    # Delete all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted: {file_path}")



def chunk_list(lst, chunk_size):
    """Split list into chunks of max chunk_size"""
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

def truncate_text(text, max_chars=8000):
    """Truncate text to avoid token limit issues (roughly estimated)"""
    return text[:max_chars]

def generate_embeddings_safely(texts,input_type):
    all_embeddings = []
    chunk_size = 70 # Cohere model limit
    model_id="cohere.embed-english-v3"
    for batch in chunk_list(texts, chunk_size):
        # Truncate any long text in batch
        batch = [truncate_text(t) for t in batch]
        response = create_cohere_embeddings(batch,input_type)
        batch_embeddings = [item['embedding'] for item in response['data']]
        all_embeddings.extend(batch_embeddings)
    
    return all_embeddings


def create_cohere_embeddings(text,input_type="search_document"):
    url=TIP_AI_URL
    api_key=TIP_AI_VIRTUAL_KEY
    print(text)
    headers = {
        'x-goog-api-key': api_key,
        'Content-Type': 'application/json'
    }
    data = {
        "input":text,
        "input_type": input_type,
        "texts":text,
    }
    response = requests.post(url, headers=headers, json=data,verify=False)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status {response.status_code}")
        print(response.text)
        return None

    
def save_embeddings(filename, embeddings):
    try:
        np.save(filename, embeddings)
        print(f"Embeddings successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving embeddings: {e}")    