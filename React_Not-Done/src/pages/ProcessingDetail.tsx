import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { useApiContext } from '../api';
import { useToast } from "../components/ui/use-toast";
import { Progress } from "../components/ui/Progress";

const ProcessingDetail = () => {
  const { jobId } = useParams();
  const apiContext = useApiContext();
  const { toast } = useToast();
  const [status, setStatus] = useState<any>(null);

  const { analysis, ws } = apiContext || {}; // Fallback to an empty object if apiContext is null

  useEffect(() => {
    // Early return if apiContext, analysis, or ws is not available
    if (!apiContext || !analysis || !ws) return;

    const unsubscribe = ws.subscribe(`job_status_${jobId}`, (status: any) => {
      setStatus(status);

      if (status.status === 'completed') {
        toast({
          title: "Analysis completed",
          description: "Your results are ready",
          variant: "success"
        });
      } else if (status.status === 'failed') {
        toast({
          title: "Analysis failed",
          description: status.error,
          variant: "destructive"
        });
      }
    });

    analysis.getStatus(jobId).then(setStatus);

    return () => unsubscribe();
  }, [jobId, analysis, ws, toast, apiContext]); // Add apiContext to the dependency array

  // Render the error message if apiContext is not available
  if (!apiContext) {
    return (
      <div className="text-red-500 text-center">
        Error: API context is not available. Please check your API provider.
      </div>
    );
  }

  return (
    <div className="space-y-8">
      {status && (
        <div className="space-y-4">
          <Progress value={status.progress} />
          <div className="text-sm text-[#a3a3a3]">
            {status.files_processed} / {status.total_files} files processed
          </div>
        </div>
      )}
    </div>
  );
};

export default ProcessingDetail;