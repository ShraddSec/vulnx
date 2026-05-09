from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uuid
import asyncio

from scanner import run_scan

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

scans = {}

class ScanRequest(BaseModel):
    url: str


@app.post("/scan")
async def start_scan(request: ScanRequest):

    scan_id = str(uuid.uuid4())

    scans[scan_id] = {
        "status": "running",
        "progress": 0,
        "logs": [],
        "result": None
    }

    asyncio.create_task(run_scan(request.url, scan_id, scans))

    return {
        "scan_id": scan_id
    }


@app.get("/scan/{scan_id}")
async def get_scan_status(scan_id: str):

    if scan_id not in scans:
        raise HTTPException(status_code=404, detail="Scan not found")

    return scans[scan_id]