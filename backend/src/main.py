from fastapi import FastAPI
from api.routes import items

app = FastAPI(title="Backend API")

app.include_router(items.router)

@app.get("/")
async def root():
    return {"message": "Backend API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
