# backend/training_service.py
from typing import List, Dict, Optional
from pathlib import Path
import json
import csv
from datetime import datetime

# Standard Library Imports
import asyncio
import shutil

# Import from markdown_analyzer
from ..markdown_analyzer import (
    MarkdownAnalyzer,
    DocumentProcessor,
    TrainingDataProcessor,
    DatasetValidator,
    DocumentStructure,
)

from .models import (
    TrainingExample,
    ProcessingResult,
    ValidationError,
    FileInfo,
    AnalysisConfig
)

class TrainingDataService:
    """
    Service för hantering av träningsdata
    """
    
    def __init__(self, output_dir: str = "./output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    async def save_training_data(
        self,
        job_id: str,
        results: List[ProcessingResult]
    ) -> Dict[str, List[str]]:
        """
        Sparar träningsdata från analysresultat
        """
        # Samla alla träningsexempel
        training_examples = []
        for result in results:
            if 'training_examples' in result.extracted_data:
                training_examples.extend(
                    result.extracted_data['training_examples']
                )

        # Gruppera efter kommando
        examples_by_command = {}
        for example in training_examples:
            if example.command not in examples_by_command:
                examples_by_command[example.command] = []
            examples_by_command[example.command].append(example)

        # Spara data i olika format
        output_files = {
            'json': [],
            'csv': []
        }

        # Skapa jobbspecifik katalog
        job_dir = self.output_dir / job_id
        job_dir.mkdir(exist_ok=True)

        # Spara för varje kommando
        for command, examples in examples_by_command.items():
            # JSON format
            json_file = job_dir / f"training_data_{command}.json"
            await self._save_json(examples, json_file)
            output_files['json'].append(str(json_file))

            # CSV format
            csv_file = job_dir / f"training_data_{command}.csv"
            await self._save_csv(examples, csv_file)
            output_files['csv'].append(str(csv_file))

        return output_files

    async def _save_json(
        self,
        examples: List[TrainingExample],
        file_path: Path
    ) -> None:
        """
        Sparar träningsexempel i JSON-format
        """
        data = [example.dict() for example in examples]
        await self._write_json(data, file_path)

    async def _save_csv(
        self,
        examples: List[TrainingExample],
        file_path: Path
    ) -> None:
        """
        Sparar träningsexempel i CSV-format
        """
        fieldnames = ['command', 'article_number', 'user_input', 'ai_output']
        rows = [
            {
                'command': ex.command,
                'article_number': ex.article_number,
                'user_input': ex.user_input,
                'ai_output': ex.ai_output
            }
            for ex in examples
        ]
        
        await self._write_csv(rows, fieldnames, file_path)

    async def _write_json(self, data: Dict, file_path: Path) -> None:
        """
        Skriver JSON-data till fil asynkront
        """
        json_str = json.dumps(data, ensure_ascii=False, indent=2)
        await self._write_file(file_path, json_str)

    async def _write_csv(
        self,
        rows: List[Dict],
        fieldnames: List[str],
        file_path: Path
    ) -> None:
        """
        Skriver CSV-data till fil asynkront
        """
        csv_data = []
        # Skriv header
        csv_data.append(','.join(fieldnames))
        
        # Skriv rader
        for row in rows:
            csv_row = [
                f'"{str(row[field]).replace('"', '""')}"'
                for field in fieldnames
            ]
            csv_data.append(','.join(csv_row))
        
        await self._write_file(file_path, '\n'.join(csv_data))

    async def _write_file(self, file_path: Path, content: str) -> None:
        """
        Skriver innehåll till fil asynkront
        """
        await asyncio.to_thread(
            file_path.write_text,
            content,
            encoding='utf-8'
        )

    async def load_training_data(
        self,
        job_id: str,
        command: Optional[str] = None,
        format: str = 'json'
    ) -> List[TrainingExample]:
        """
        Läser in sparad träningsdata
        """
        job_dir = self.output_dir / job_id
        if not job_dir.exists():
            raise FileNotFoundError(f"No data found for job {job_id}")

        if format == 'json':
            return await self._load_json(job_dir, command)
        elif format == 'csv':
            return await self._load_csv(job_dir, command)
        else:
            raise ValueError(f"Unsupported format: {format}")

    async def _load_json(
        self,
        job_dir: Path,
        command: Optional[str]
    ) -> List[TrainingExample]:
        """
        Läser träningsdata från JSON-filer
        """
        examples = []
        
        if command:
            # Läs specifikt kommando
            json_file = job_dir / f"training_data_{command}.json"
            if json_file.exists():
                data = json.loads(await self._read_file(json_file))
                examples.extend([TrainingExample(**ex) for ex in data])
        else:
            # Läs alla JSON-filer
            for json_file in job_dir.glob("training_data_*.json"):
                data = json.loads(await self._read_file(json_file))
                examples.extend([TrainingExample(**ex) for ex in data])
        
        return examples

    async def _load_csv(
        self,
        job_dir: Path,
        command: Optional[str]
    ) -> List[TrainingExample]:
        """
        Läser träningsdata från CSV-filer
        """
        examples = []
        
        if command:
            # Läs specifikt kommando
            csv_file = job_dir / f"training_data_{command}.csv"
            if csv_file.exists():
                examples.extend(
                    await self._read_csv_file(csv_file)
                )
        else:
            # Läs alla CSV-filer
            for csv_file in job_dir.glob("training_data_*.csv"):
                examples.extend(
                    await self._read_csv_file(csv_file)
                )
        
        return examples

    async def _read_csv_file(self, file_path: Path) -> List[TrainingExample]:
        """
        Läser och parsar en CSV-fil
        """
        content = await self._read_file(file_path)
        reader = csv.DictReader(content.splitlines())
        
        return [TrainingExample(**row) for row in reader]

    async def _read_file(self, file_path: Path) -> str:
        """
        Läser en fil asynkront
        """
        return await asyncio.to_thread(
            file_path.read_text,
            encoding='utf-8'
        )

# backend/analyzer_service.py (uppdatering)
class AnalyzerService:
    def __init__(self):
        self.analyzer = MarkdownAnalyzer()
        self.document_processor = DocumentProcessor(self.analyzer.extractors)
        self.training_processor = TrainingDataProcessor()
        self.validator = DatasetValidator()
        self.training_service = TrainingDataService()
        
        # Statushantering
        self.active_processes: Dict[str, asyncio.Task] = {}
        self.file_status: Dict[str, FileInfo] = {}
        self.job_progress: Dict[str, float] = {}
        
        # Callback-hantering
        self.status_callbacks: List[callable] = []

    def register_status_callback(self, callback: callable) -> None:
        """Registrera callback för statusuppdateringar"""
        self.status_callbacks.append(callback)

    async def _notify_status_update(self, job_id: str, status: Dict) -> None:
        """Notifiera alla registrerade callbacks om statusuppdateringar"""
        for callback in self.status_callbacks:
            try:
                await callback(job_id, status)
            except Exception as e:
                print(f"Error in status callback: {str(e)}")

    async def process_files(
        self,
        job_id: str,
        files: List[FileInfo],
        config: AnalysisConfig
    ) -> List[ProcessingResult]:
        """
        Processar en lista med filer och genererar träningsdata
        """
        results = []
        total_files = len(files)
        
        for i, file_info in enumerate(files):
            try:
                # Uppdatera status
                progress = (i / total_files) * 100
                await self._update_job_status(
                    job_id,
                    {
                        'status': 'processing',
                        'progress': progress,
                        'current_file': file_info.name,
                        'files_processed': i,
                        'total_files': total_files
                    }
                )
                
                # Processa fil
                doc = await self._process_document(file_info)
                
                # Generera träningsdata för varje kommando
                training_examples = []
                for cmd in config.commands:
                    examples = self._generate_training_data(doc, [cmd])
                    if examples:
                        training_examples.extend(examples)
                
                # Validera träningsdata
                validation_result = self.validator.validate_training_samples(
                    training_examples
                )
                
                # Skapa resultat
                result = ProcessingResult(
                    file_id=file_info.id,
                    article_number=doc.article_number,
                    product_name=doc.product_name,
                    extracted_data={
                        'training_examples': training_examples,
                        'validation': validation_result.dict()
                    },
                    warnings=validation_result.warnings,
                    errors=validation_result.errors,
                    processing_time=0  # Implementera tidtagning
                )
                
                results.append(result)
                
            except Exception as e:
                print(f"Error processing {file_info.name}: {str(e)}")
                file_info.status = 'failed'
                file_info.error = str(e)
                
                # Notifiera om felet
                await self._notify_status_update(
                    job_id,
                    {
                        'error': str(e),
                        'failed_file': file_info.name
                    }
                )
        
        # Spara träningsdata
        try:
            output_files = await self.training_service.save_training_data(
                job_id,
                results
            )
            
            # Uppdatera slutstatus
            await self._update_job_status(
                job_id,
                {
                    'status': 'completed',
                    'progress': 100,
                    'files_processed': total_files,
                    'output_files': output_files
                }
            )
            
        except Exception as e:
            print(f"Error saving training data: {str(e)}")
            await self._update_job_status(
                job_id,
                {
                    'status': 'failed',
                    'error': f"Failed to save training data: {str(e)}"
                }
            )
        
        return results

    async def _update_job_status(self, job_id: str, status_update: Dict) -> None:
        """
        Uppdaterar och notifierar om jobbstatus
        """
        # Uppdatera intern status
        if job_id not in self.job_progress:
            self.job_progress[job_id] = {}
        
        self.job_progress[job_id].update(status_update)
        
        # Notifiera om uppdateringen
        await self._notify_status_update(job_id, self.job_progress[job_id])

    async def get_job_status(self, job_id: str) -> Dict:
        """
        Hämtar aktuell status för ett jobb
        """
        if job_id not in self.job_progress:
            raise KeyError(f"No such job: {job_id}")
        
        return self.job_progress[job_id]

    async def cancel_job(self, job_id: str) -> None:
        """
        Avbryter ett pågående jobb
        """
        if job_id in self.active_processes:
            # Avbryt process
            self.active_processes[job_id].cancel()
            
            # Uppdatera status
            await self._update_job_status(
                job_id,
                {
                    'status': 'cancelled',
                    'error': 'Job cancelled by user'
                }
            )
            
            # Ta bort från aktiva processer
            del self.active_processes[job_id]

    async def cleanup_job(self, job_id: str) -> None:
        """
        Rensar temporära filer för ett jobb
        """
        job_dir = Path(f"temp/{job_id}")
        if job_dir.exists():
            await asyncio.to_thread(shutil.rmtree, str(job_dir))

    def _generate_training_data(
        self,
        doc: 'DocumentStructure',
        commands: List[str]
    ) -> List[TrainingExample]:
        """
        Genererar träningsdata för specifika kommandon
        """
        examples = []
        
        for cmd in commands:
            if cmd == 'f':
                examples.extend(self._generate_full_info_examples(doc))
            elif cmd == 's':
                examples.extend(self._generate_summary_examples(doc))
            elif cmd == 't':
                examples.extend(self._generate_technical_examples(doc))
            elif cmd == 'c':
                examples.extend(self._generate_compatibility_examples(doc))
        
        return examples

    def _generate_full_info_examples(self, doc: 'DocumentStructure') -> List[TrainingExample]:
        """Genererar träningsexempel för -f kommandot"""
        return self.training_processor.create_examples_for_command(doc, 'f')

    def _generate_summary_examples(self, doc: 'DocumentStructure') -> List[TrainingExample]:
        """Genererar träningsexempel för -s kommandot"""
        return self.training_processor.create_examples_for_command(doc, 's')

    def _generate_technical_examples(self, doc: 'DocumentStructure') -> List[TrainingExample]:
        """Genererar träningsexempel för -t kommandot"""
        return self.training_processor.create_examples_for_command(doc, 't')

    def _generate_compatibility_examples(self, doc: 'DocumentStructure') -> List[TrainingExample]:
        """Genererar träningsexempel för -c kommandot"""
        return self.training_processor.create_examples_for_command(doc, 'c')