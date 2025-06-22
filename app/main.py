from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Agent Bridge API")

app.include_router(router)

@app.get("/health")
async def health_check():
    return {"status": "ok"}
