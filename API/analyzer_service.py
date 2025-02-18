# backend/analyzer_service.py

from fastapi import FastAPI, UploadFile, File, WebSocket, BackgroundTasks, HTTPException
from typing import List, Dict, Optional
from pathlib import Path
import asyncio
from datetime import datetime
from uuid import uuid4

app = FastAPI(title="Markdown Analyzer API")

from .models import (
    AnalysisConfig,
    ProcessingResult,
    TrainingExample,
    FileInfo
)


from ..markdown_analyzer import (
    MarkdownAnalyzer,
    DocumentProcessor,
    TrainingDataProcessor,
    DatasetValidator,
    DocumentStructure
)

class AnalyzerService:
    """
    Service-klass som kopplar ihop MarkdownAnalyzer med API:et
    """
    
    def __init__(self):
        self.analyzer = MarkdownAnalyzer()
        self.document_processor = DocumentProcessor(self.analyzer.extractors)
        self.training_processor = TrainingDataProcessor()
        self.validator = DatasetValidator()
        
        # Håll koll på aktiva processer
        self.active_processes: Dict[str, asyncio.Task] = {}
        self.file_status: Dict[str, FileInfo] = {}

    async def process_files(
        self,
        files: List[FileInfo],
        config: AnalysisConfig,
        progress_callback: Optional[callable] = None
    ) -> List[ProcessingResult]:
        """
        Processar en lista med filer med given konfiguration
        """
        results = []
        total_files = len(files)
        
        for i, file_info in enumerate(files):
            try:
                # Uppdatera filstatus
                self.file_status[file_info.id].status = "processing"
                
                # Processa dokumentet
                doc = await self._process_document(file_info)
                
                # Generera träningsdata
                training_examples = self._generate_training_data(
                    doc, 
                    config.commands
                )
                
                # Validera resultat
                validation_result = self.validator.validate_training_samples(
                    training_examples
                )

                # Skapa processresultat
                result = ProcessingResult(
                    file_id=file_info.id,
                    article_number=doc.article_number,
                    product_name=doc.product_name,
                    extracted_data={
                        'training_examples': training_examples,
                        'validation': validation_result
                    },
                    warnings=validation_result.warnings,
                    errors=validation_result.errors,
                    processing_time=0  # Implementera tidtagning
                )
                
                results.append(result)
                
                # Uppdatera status
                self.file_status[file_info.id].status = "completed"
                
                # Rapportera progress
                if progress_callback:
                    progress = (i + 1) / total_files * 100
                    await progress_callback(progress, file_info.name)
                    
            except Exception as e:
                # Hantera fel
                self.file_status[file_info.id].status = "failed"
                self.file_status[file_info.id].error = str(e)
                
                # Logga felet
                print(f"Error processing {file_info.name}: {str(e)}")
        
        return results

    async def _process_document(self, file_info: FileInfo) -> 'DocumentStructure':
        """
        Processar ett enskilt dokument asynkront
        """
        # Läs filinnehåll
        file_path = Path(f"temp/{file_info.id}_{file_info.name}")
        content = await self._read_file(file_path)
        
        # Processa dokumentet
        return self.document_processor.process_document(content)

    def _generate_training_data(
        self,
        doc: 'DocumentStructure',
        commands: List[str]
    ) -> List[TrainingExample]:
        """
        Genererar träningsdata för angivna kommandon
        """
        return self.training_processor.create_training_examples(doc, commands)

    async def _read_file(self, path: Path) -> str:
        """
        Läser en fil asynkront
        """
        return await asyncio.to_thread(path.read_text, encoding='utf-8')

    def start_analysis(self, job_id: str, config: AnalysisConfig) -> None:
        """
        Startar en ny analysprocess
        """
        # Skapa och spara asyncio task
        task = asyncio.create_task(
            self._run_analysis(job_id, config)
        )
        self.active_processes[job_id] = task

    async def _run_analysis(self, job_id: str, config: AnalysisConfig) -> None:
        """
        Kör analysprocessen i bakgrunden
        """
        try:
            # Hämta filer att processa
            files = [
                self.file_status[file_id]
                for file_id in config.files
                if file_id in self.file_status
            ]
            
            # Processa filer
            results = await self.process_files(files, config)
            
            # Spara resultat
            await self._save_results(job_id, results)
            
        except Exception as e:
            # Hantera fel
            print(f"Analysis failed for job {job_id}: {str(e)}")
            raise

    async def _save_results(
        self,
        job_id: str,
        results: List[ProcessingResult]
    ) -> None:
        """
        Sparar analysresultat
        """
        # Implementera resultatlagring här
        pass


# Skapa analyzer service vid uppstart
analyzer_service = AnalyzerService()

@app.post("/api/analysis/start")
async def start_analysis(
    config: AnalysisConfig,
    background_tasks: BackgroundTasks
):
    """Starta ny analys"""
    job_id = str(uuid4())
    
    # Starta analys via service
    analyzer_service.start_analysis(job_id, config)
    
    return {"job_id": job_id}

@app.post("/api/files/upload")
async def upload_files(files: List[UploadFile] = File(...)):
    """Hantera filuppladdning"""
    uploaded_files = []
    
    for file in files:
        # Skapa fil-ID och spara information
        file_id = str(uuid4())
        file_info = FileInfo(
            id=file_id,
            name=file.filename,
            size=0,  # Uppdateras efter uppladdning
            status="pending"
        )
        analyzer_service.file_status[file_id] = file_info
        
        # Spara fil
        content = await file.read()
        file_info.size = len(content)
        
        file_path = f"temp/{file_id}_{file.filename}"
        with open(file_path, "wb") as f:
            f.write(content)
        
        uploaded_files.append(file_info)
    
    return {"files": uploaded_files}