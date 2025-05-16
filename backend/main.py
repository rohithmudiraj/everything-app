from fastapi import FastAPI
from app.routes import router
from app.services import initialize_search_engine

app = FastAPI()

# Include router
app.include_router(router)

@app.on_event("startup")
def startup():
    try:
        initialize_search_engine()  # This sets search_engine inside services.py
    except Exception as e:
        print(f"Error initializing search engine: {e}")
        raise e  # Stops app from starting if init fails
