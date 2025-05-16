from fastapi import APIRouter, Depends
from app.services import get_search_engine  # Import from services
from utils import  generate_embeddings
from app.search import SemanticSearch
from app.services import initialize_search_engine
router = APIRouter()

@router.get("/query/")
def query_data(query: str, search_engine: SemanticSearch = Depends(get_search_engine)):
    if search_engine is None:
        raise HTTPException(status_code=500, detail="Search engine not initialized")
    # Otherwise, semantic
    embedding = generate_embeddings([query], "search_query")[0]
    results = search_engine.query(embedding)
    return results.to_dict(orient="records")


@router.get("/re-generate")
def regenerate():
    initialize_search_engine(False)
