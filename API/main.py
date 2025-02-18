# backend/main.py
from fastapi import FastAPI, UploadFile, File, WebSocket, BackgroundTasks, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict
import uvicorn
import asyncio
import json
from datetime import datetime
from uuid import uuid4

from ..markdown_analyzer import *
from .models import (
    AnalysisConfig,
    AnalysisStatus,
    AnalysisResult,
    JobStats,
    SystemStatus
)

app = FastAPI(title="Markdown Analyzer API")

# CORS-konfiguration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory datalagring (i produktion skulle detta vara en databas)
active_jobs = {}
job_statuses = {}
job_results = {}
connected_clients = set()

# Bakgrundsarbetare för analysprocessen
async def process_analysis(job_id: str, config: AnalysisConfig, files: List[str]):
    try:
        analyzer = MarkdownAnalyzer()
        total_files = len(files)
        
        # Uppdatera status till processing
        job_statuses[job_id] = AnalysisStatus(
            job_id=job_id,
            status="processing",
            progress=0,
            files_processed=0,
            total_files=total_files,
            start_time=datetime.now().isoformat()
        )
        
        # Notifiera alla anslutna klienter
        await broadcast_status(job_id)
        
        results = []
        for idx, file in enumerate(files):
            try:
                # Process file
                result = analyzer.process_file(file)
                results.append(result)
                
                # Uppdatera status
                progress = (idx + 1) / total_files * 100
                job_statuses[job_id].files_processed = idx + 1
                job_statuses[job_id].progress = progress
                job_statuses[job_id].current_file = file
                
                await broadcast_status(job_id)
                
            except Exception as e:
                print(f"Error processing file {file}: {str(e)}")
        
        # Generera träningsdata
        training_data = analyzer.generate_training_data(
            results, config.commands
        )
        
        # Spara resultat
        job_results[job_id] = AnalysisResult(
            job_id=job_id,
            files_processed=total_files,
            success_count=len(results),
            error_count=0,
            warnings=[],
            output_files=[],
            processing_time=0  # Beräkna faktisk tid
        )
        
        # Uppdatera slutstatus
        job_statuses[job_id].status = "completed"
        await broadcast_status(job_id)
        
    except Exception as e:
        # Hantera fel
        job_statuses[job_id].status = "failed"
        job_statuses[job_id].error = str(e)
        await broadcast_status(job_id)
        raise

# WebSocket-hantering
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.add(websocket)
    try:
        while True:
            await websocket.receive_text()
    except:
        connected_clients.remove(websocket)

async def broadcast_status(job_id: str):
    """Skickar statusuppdateringar till alla anslutna klienter"""
    if job_id in job_statuses:
        status = job_statuses[job_id]
        message = {
            "type": f"job_status_{job_id}",
            "payload": status.dict()
        }
        for client in connected_clients:
            try:
                await client.send_json(message)
            except:
                connected_clients.remove(client)

# API Endpoints

@app.post("/api/files/upload")
async def upload_files(files: List[UploadFile] = File(...)):
    """Hantera filuppladdning"""
    uploaded_files = []
    for file in files:
        # Spara fil temporärt
        file_id = str(uuid4())
        file_path = f"temp/{file_id}_{file.filename}"
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        uploaded_files.append({
            "id": file_id,
            "name": file.filename,
            "size": len(content)
        })
    return {"files": uploaded_files}

@app.post("/api/analysis/start")
async def start_analysis(
    config: AnalysisConfig,
    background_tasks: BackgroundTasks
):
    """Starta ny analys"""
    job_id = str(uuid4())
    active_jobs[job_id] = config
    
    # Starta analys i bakgrunden
    background_tasks.add_task(
        process_analysis,
        job_id,
        config,
        config.files
    )
    
    return {"job_id": job_id}

@app.get("/api/analysis/status/{job_id}")
async def get_analysis_status(job_id: str):
    """Hämta status för specifik analys"""
    if job_id not in job_statuses:
        raise HTTPException(status_code=404, detail="Job not found")
    return job_statuses[job_id]

@app.post("/api/analysis/cancel/{job_id}")
async def cancel_analysis(job_id: str):
    """Avbryt pågående analys"""
    if job_id not in active_jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    
    # Implementera avbrytningslogik här
    job_statuses[job_id].status = "cancelled"
    await broadcast_status(job_id)
    
    return {"status": "cancelled"}

@app.get("/api/results/{job_id}")
async def get_results(job_id: str):
    """Hämta analysresultat"""
    if job_id not in job_results:
        raise HTTPException(status_code=404, detail="Results not found")
    return job_results[job_id]

@app.get("/api/results/{job_id}/export")
async def export_results(job_id: str, format: str):
    """Exportera resultat i specifikt format"""
    if job_id not in job_results:
        raise HTTPException(status_code=404, detail="Results not found")
    
    result = job_results[job_id]
    if format == "json":
        return result.dict()
    elif format == "csv":
        # Implementera CSV-export
        pass
    else:
        raise HTTPException(status_code=400, detail="Unsupported format")

@app.get("/api/jobs/active")
async def get_active_jobs():
    """Hämta aktiva jobb"""
    return [
        {
            "job_id": job_id,
            "status": job_statuses[job_id]
        }
        for job_id in active_jobs
        if job_statuses[job_id].status == "processing"
    ]

@app.get("/api/jobs/stats")
async def get_job_stats():
    """Hämta jobbstatistik"""
    total_jobs = len(job_statuses)
    completed_jobs = len([
        job_id for job_id in job_statuses
        if job_statuses[job_id].status == "completed"
    ])
    
    return JobStats(
        active_jobs=len(active_jobs),
        completed_jobs=completed_jobs,
        total_jobs=total_jobs,
        success_rate=completed_jobs/total_jobs if total_jobs > 0 else 0
    )

@app.get("/api/system/status")
async def get_system_status():
    """Hämta systemstatus"""
    return SystemStatus(
        connected=True,
        workers=4,  # Konfigurerbart
        memory_usage=0.5,  # Implementera faktisk mätning
        cpu_usage=0.3,  # Implementera faktisk mätning
        uptime=3600  # Implementera faktisk mätning
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)