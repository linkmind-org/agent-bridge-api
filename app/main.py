from fastapi import FastAPI
from app.api.routes import router
from app.db.database import engine, metadata

app = FastAPI(title="Agent Bridge API")

# Create tables if they don't exist yet
metadata.create_all(bind=engine)

# Include API router(s)
app.include_router(router)

# Root endpoint with friendly message
@app.get("/")
async def root():
    return {
        "message": "Agent Bridge API is running. Visit /docs for API documentation."
    }

# Healthcheck endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok"}