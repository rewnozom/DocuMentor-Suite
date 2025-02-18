// src/api/index.js
import axios from 'axios';
import React, { createContext, useContext, useEffect, useState } from 'react';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

// Skapa axios-instans med grundkonfiguration
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// -------------------------
// API-endpoints för filhantering
export const fileApi = {
  // Ladda upp filer för analys
  uploadFiles: async (files) => {
    const formData = new FormData();
    files.forEach(file => formData.append('files', file));
    
    const response = await api.post('/files/upload', formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    });
    return response.data;
  },
  // Hämta lista över tillgängliga filer
  getFiles: async () => {
    const response = await api.get('/files');
    return response.data;
  }
};

// -------------------------
// API-endpoints för analyskonfiguration
export const analysisApi = {
  // Starta analys med specifik konfiguration
  startAnalysis: async (config) => {
    const response = await api.post('/analysis/start', config);
    return response.data;
  },
  // Hämta status för pågående analys
  getStatus: async (jobId) => {
    const response = await api.get(`/analysis/status/${jobId}`);
    return response.data;
  },
  // Avbryt pågående analys
  cancelAnalysis: async (jobId) => {
    const response = await api.post(`/analysis/cancel/${jobId}`);
    return response.data;
  }
};

// -------------------------
// API-endpoints för resultathantering
export const resultsApi = {
  // Hämta analysresultat
  getResults: async (jobId) => {
    const response = await api.get(`/results/${jobId}`);
    return response.data;
  },
  // Exportera resultat i specifikt format
  exportResults: async (jobId, format) => {
    const response = await api.get(`/results/${jobId}/export`, {
      params: { format },
      responseType: 'blob'
    });
    return response.data;
  }
};

// -------------------------
// API-endpoints för jobbhantering
export const jobsApi = {
  // Hämta aktiva jobb
  getActiveJobs: async () => {
    const response = await api.get('/jobs/active');
    return response.data;
  },
  // Hämta köade jobb
  getQueuedJobs: async () => {
    const response = await api.get('/jobs/queued');
    return response.data;
  },
  // Hämta slutförda jobb
  getCompletedJobs: async () => {
    const response = await api.get('/jobs/completed');
    return response.data;
  },
  // Hämta jobbstatistik
  getJobStats: async () => {
    const response = await api.get('/jobs/stats');
    return response.data;
  }
};

// -------------------------
// API-endpoints för systemstatus
export const systemApi = {
  // Hämta systemstatus
  getStatus: async () => {
    const response = await api.get('/system/status');
    return response.data;
  },
  // Hämta systemkonfiguration
  getConfig: async () => {
    const response = await api.get('/system/config');
    return response.data;
  },
  // Uppdatera systemkonfiguration
  updateConfig: async (config) => {
    const response = await api.put('/system/config', config);
    return response.data;
  }
};

// -------------------------
// API-hooks för React-komponenter
export const useApi = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const execute = async (apiFunc, ...args) => {
    try {
      setLoading(true);
      setError(null);
      const result = await apiFunc(...args);
      return result;
    } catch (err) {
      setError(err.response?.data?.message || err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  };

  return { loading, error, execute };
};

// -------------------------
// WebSocket hantering för realtidsuppdateringar
export class WebSocketClient {
  constructor() {
    this.ws = null;
    this.subscribers = new Map();
  }

  connect() {
    this.ws = new WebSocket(`ws://${API_BASE_URL.replace('http://', '')}/ws`);

    this.ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      const subscribers = this.subscribers.get(data.type) || [];
      subscribers.forEach(callback => callback(data.payload));
    };

    this.ws.onclose = () => {
      setTimeout(() => this.connect(), 1000);
    };
  }

  subscribe(type, callback) {
    if (!this.subscribers.has(type)) {
      this.subscribers.set(type, []);
    }
    this.subscribers.get(type).push(callback);

    return () => {
      const callbacks = this.subscribers.get(type);
      const index = callbacks.indexOf(callback);
      if (index > -1) {
        callbacks.splice(index, 1);
      }
    };
  }
}

// -------------------------
// Skapa en default API-kontekst
const defaultApiContext = {
  files: fileApi,
  analysis: analysisApi,
  results: resultsApi,
  jobs: jobsApi,
  system: systemApi,
  ws: new WebSocketClient(),
  status: null,
  stats: null
};

// Skapa React Context för API-hantering
const ApiContext = createContext(defaultApiContext);

// ApiProvider-komponenten
export const ApiProvider = ({ children }) => {
  const [wsClient] = useState(() => new WebSocketClient());
  const [systemStatus, setSystemStatus] = useState(null);
  const [jobStats, setJobStats] = useState(null);

  useEffect(() => {
    wsClient.connect();

    const unsubStatus = wsClient.subscribe('system_status', (status) => {
      setSystemStatus(status);
    });

    const unsubStats = wsClient.subscribe('job_stats', (stats) => {
      setJobStats(stats);
    });

    return () => {
      unsubStatus();
      unsubStats();
    };
  }, [wsClient]);

  const apiContextValue = {
    files: fileApi,
    analysis: analysisApi,
    results: resultsApi,
    jobs: jobsApi,
    system: systemApi,
    ws: wsClient,
    status: systemStatus,
    stats: jobStats
  };

  return (
    <ApiContext.Provider value={apiContextValue}>
      {children}
    </ApiContext.Provider>
  );
};

// Exportera hook för att använda API-konteksten
export const useApiContext = () => {
  const context = useContext(ApiContext);
  if (!context) {
    console.error("useApiContext was used outside of ApiProvider!");
    return defaultApiContext;
  }
  return context;
};
