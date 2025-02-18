# backend/models.py
from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from datetime import datetime

class AnalysisConfig(BaseModel):
    """Konfiguration för analysprocess"""
    commands: List[str]
    workers: int = Field(default=4, ge=1, le=8)
    output_dir: str = "./output"
    batch_size: Optional[int] = None
    files: List[str]

class AnalysisStatus(BaseModel):
    """Status för pågående analys"""
    job_id: str
    status: str  # 'queued', 'processing', 'completed', 'failed', 'cancelled'
    progress: float
    files_processed: int
    total_files: int
    current_file: Optional[str]
    start_time: str
    estimated_completion: Optional[str]
    error: Optional[str]

class AnalysisResult(BaseModel):
    """Resultat från analys"""
    job_id: str
    files_processed: int
    success_count: int
    error_count: int
    warnings: List[str]
    output_files: List[str]
    processing_time: float  # i sekunder

class JobStats(BaseModel):
    """Statistik för jobb"""
    active_jobs: int
    completed_jobs: int
    total_jobs: int
    success_rate: float

class SystemStatus(BaseModel):
    """Systemstatus"""
    connected: bool
    workers: int
    memory_usage: float  # 0-1
    cpu_usage: float  # 0-1
    uptime: int  # sekunder

class TrainingExample(BaseModel):
    """Ett träningsexempel"""
    user_input: str
    ai_output: str
    command: str
    article_number: str
    confidence: float = 1.0

class ValidationError(BaseModel):
    """Valideringsfel"""
    field: str
    message: str

class ApiResponse(BaseModel):
    """Standardiserad API-respons"""
    success: bool
    data: Optional[Dict] = None
    error: Optional[str] = None
    warnings: List[str] = []
    validation_errors: List[ValidationError] = []

# Hjälpklasser för filhantering
class FileInfo(BaseModel):
    """Information om en uppladdad fil"""
    id: str
    name: str
    size: int
    upload_time: datetime = Field(default_factory=datetime.now)
    status: str = "pending"  # 'pending', 'processing', 'completed', 'failed'
    error: Optional[str] = None

class ProcessingResult(BaseModel):
    """Resultat från filprocessering"""
    file_id: str
    article_number: Optional[str]
    product_name: Optional[str]
    extracted_data: Dict
    warnings: List[str] = []
    errors: List[str] = []
    processing_time: float

# WebSocket-meddelanden
class WebSocketMessage(BaseModel):
    """Basmodell för WebSocket-meddelanden"""
    type: str
    payload: Dict

class StatusUpdate(BaseModel):
    """Statusuppdatering för WebSocket"""
    job_id: str
    status: str
    progress: float
    message: Optional[str]
    timestamp: datetime = Field(default_factory=datetime.now)

# Konfigurationsmodeller
class WorkerConfig(BaseModel):
    """Konfiguration för arbetare"""
    num_workers: int = Field(default=4, ge=1, le=8)
    batch_size: int = Field(default=10, ge=1)
    timeout: int = Field(default=300, ge=30)  # sekunder

class OutputConfig(BaseModel):
    """Konfiguration för output"""
    base_dir: str = "./output"
    file_format: str = "json"
    compress: bool = False
    max_file_size: int = Field(default=10_485_760)  # 10MB

class SystemConfig(BaseModel):
    """Systemkonfiguration"""
    worker_config: WorkerConfig
    output_config: OutputConfig
    debug_mode: bool = False
    log_level: str = "INFO"