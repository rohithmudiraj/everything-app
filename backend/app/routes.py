from fastapi import APIRouter, Depends
from app.services import get_search_engine  # Import from services
from utils import  generate_embeddings
from app.search import SemanticSearch
from app.services import initialize_search_engine
import pandas as pd
import numpy as np
router = APIRouter()

@router.get("/query/")
def query_data(query: str, search_engine: SemanticSearch = Depends(get_search_engine)):
    if search_engine is None:
        raise HTTPException(status_code=500, detail="Search engine not initialized")
    # Otherwise, semantic
    embedding = generate_embeddings([query], "search_query")[0]
    results = search_engine.query(embedding)
        # 1. Replace inf and -inf with np.nan
    results = results.replace([np.inf, -np.inf], np.nan)
    # 2. Replace np.nan with None for JSON compatibility
    results = results.where(pd.notnull(results), None)
    # 3. Convert to list of dicts (records)
    records = results.to_dict(orient="records")
    # 4. Optional but extra safe: Ensure no remaining float NaNs in nested data
    def clean_json_value(val):
        if isinstance(val, float) and (np.isnan(val) or val in [np.inf, -np.inf]):
            return None
        return val
    # Apply cleaner per-record
    json_safe_output = [
        {k: clean_json_value(v) for k, v in row.items()}
        for row in records
    ]
    return json_safe_output
