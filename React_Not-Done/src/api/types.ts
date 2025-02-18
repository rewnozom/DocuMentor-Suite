
// TypeScript typer för API-data
export interface SystemStatus {
  connected: boolean;
  workers: number;
  memory_usage: number;
  cpu_usage: number;
  uptime: number;
}

export interface JobStats {
  active_jobs: number;
  queued_jobs: number;
  completed_jobs: number;
  success_rate: number;
  average_processing_time: number;
}

export interface AnalysisConfig {
  commands: string[];
  workers: number;
  output_dir: string;
  batch_size?: number;
}

export interface AnalysisStatus {
  job_id: string;
  status: 'queued' | 'processing' | 'completed' | 'failed';
  progress: number;
  current_file?: string;
  files_processed: number;
  total_files: number;
  start_time: string;
  estimated_completion?: string;
  error?: string;
}

export interface AnalysisResult {
  job_id: string;
  files_processed: number;
  success_count: number;
  error_count: number;
  warnings: string[];
  output_files: string[];
  processing_time: number;
}