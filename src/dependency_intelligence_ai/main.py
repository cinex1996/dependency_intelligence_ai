from fastapi import FastAPI
from dependency_intelligence_ai.schemas.scan import ScanRequest
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/scan")
async def scan(scanRequest: ScanRequest):
    return scanRequest