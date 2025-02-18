// src/pages/Results.tsx
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { useApiContext } from '../api';
import { useToast } from "../components/ui/use-toast";
import { Button } from "../components/ui/Button";

const Results = () => {
  const { jobId } = useParams();
  const { results } = useApiContext();
  const { toast } = useToast();
  const [analysisResults, setAnalysisResults] = useState<any>(null);

  useEffect(() => {
    results.getResults(jobId)
      .then(setAnalysisResults)
      .catch((error: any) => {
        toast({
          title: "Failed to load results",
          description: error.message,
          variant: "destructive"
        });
      });
  }, [jobId, results, toast]);

  const handleExport = async (format: string) => {
    try {
      const blob = await results.exportResults(jobId, format);
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `analysis_results.${format}`;
      a.click();
    } catch (error: any) {
      toast({
        title: "Export failed",
        description: error.message,
        variant: "destructive"
      });
    }
  };

  return (
    <div className="space-y-8">
      {analysisResults && (
        <div className="grid gap-6">
          {/* Placeholder-komponenter – ersätt med din egen implementation */}
          <ResultsSummary results={analysisResults} />
          <ResultsDetails results={analysisResults} />
          <ExportOptions onExport={handleExport} />
        </div>
      )}
    </div>
  );
};

// Exempel på placeholder-komponenter
const ResultsSummary = ({ results }: { results: any }) => (
  <div className="p-4 bg-[#242424] rounded-lg">
    <h2 className="text-xl font-bold">Results Summary</h2>
    <pre>{JSON.stringify(results.summary, null, 2)}</pre>
  </div>
);

const ResultsDetails = ({ results }: { results: any }) => (
  <div className="p-4 bg-[#242424] rounded-lg">
    <h2 className="text-xl font-bold">Results Details</h2>
    <pre>{JSON.stringify(results.details, null, 2)}</pre>
  </div>
);

const ExportOptions = ({ onExport }: { onExport: (format: string) => void }) => (
  <div className="space-y-2">
    <h2 className="text-xl font-bold">Export Options</h2>
    <div className="flex space-x-2">
      <Button onClick={() => onExport('csv')}>Export CSV</Button>
      <Button onClick={() => onExport('json')}>Export JSON</Button>
    </div>
  </div>
);

export default Results;
