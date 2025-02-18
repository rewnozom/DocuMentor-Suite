// Anpassade felklasser
export class ApiError extends Error {
    constructor(message: string, public status?: number) {
      super(message);
      this.name = 'ApiError';
    }
  }
  
  export class NetworkError extends ApiError {
    constructor(message = 'Network error occurred') {
      super(message);
      this.name = 'NetworkError';
    }
  }
  
  export class ValidationError extends ApiError {
    constructor(message: string, public fields?: Record<string, string>) {
      super(message);
      this.name = 'ValidationError';
    }
  }