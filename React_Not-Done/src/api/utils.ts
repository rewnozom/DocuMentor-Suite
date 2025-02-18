// src/api/utils.ts
import { ApiError, NetworkError, ValidationError } from './errors';

// Hjälpfunktioner för API-hantering
export const handleApiError = (error: any) => {
  if (error.response) {
    // Server returnerade felkod
    const message = error.response.data?.message || 'An error occurred';
    const status = error.response.status;
    
    switch (status) {
      case 400:
        throw new ValidationError(message, error.response.data?.fields);
      case 401:
        // Hantera autentiseringsfel
        break;
      case 404:
        throw new ApiError(`Resource not found: ${message}`, status);
      default:
        throw new ApiError(message, status);
    }
  } else if (error.request) {
    // Ingen respons mottagen
    throw new NetworkError();
  } else {
    // Något gick fel vid uppsättning av förfrågan
    throw new ApiError('Failed to make request');
  }
};

export const formatBytes = (bytes: number): string => {
  if (bytes === 0) return '0 Bytes';
  const k = 1024;
  const sizes = ['Bytes', 'KB', 'MB', 'GB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return `${parseFloat((bytes / Math.pow(k, i)).toFixed(2))} ${sizes[i]}`;
};

export const formatDuration = (seconds: number): string => {
  if (seconds < 60) return `${seconds}s`;
  const minutes = Math.floor(seconds / 60);
  const remainingSeconds = seconds % 60;
  return `${minutes}m ${remainingSeconds}s`;
};
