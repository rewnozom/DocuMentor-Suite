// src/pages/ProcessingDashboard.tsx
import React, { useState } from 'react';
import { Card } from "../components/ui/card";
import { Button } from "../components/ui/Button";
import { Activity, AlertCircle, FileText, CheckCircle, Clock, RotateCw } from 'lucide-react';

const ProcessingDashboard = () => {
  const [activeJobs, setActiveJobs] = useState<any[]>([]);
  const [completedJobs, setCompletedJobs] = useState<any[]>([]);
  const [queuedJobs, setQueuedJobs] = useState<any[]>([]);

  const processingStats = {
    activeWorkers: 4,
    queueLength: 2,
    averageTime: '1.2s',
    successRate: '98.5%'
  };

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-3xl font-bold mb-2">Processing Status</h1>
        <p className="text-[#a3a3a3]">Monitor and manage processing jobs</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <StatCard 
          icon={<Activity className="text-[#ff6b2b]" />}
          label="Active Workers"
          value={processingStats.activeWorkers}
        />
        <StatCard 
          icon={<Clock className="text-[#ff6b2b]" />}
          label="Queue Length"
          value={processingStats.queueLength}
        />
        <StatCard 
          icon={<CheckCircle className="text-[#ff6b2b]" />}
          label="Success Rate"
          value={processingStats.successRate}
        />
        <StatCard 
          icon={<Clock className="text-[#ff6b2b]" />}
          label="Avg. Processing Time"
          value={processingStats.averageTime}
        />
      </div>

      <Card className="p-6 bg-[#242424] border-[#333333]">
        <div className="flex items-center justify-between mb-6">
          <div>
            <h2 className="text-xl font-semibold">Active Jobs</h2>
            <p className="text-sm text-[#a3a3a3] mt-1">Currently processing</p>
          </div>
          <Activity className="h-5 w-5 text-[#a3a3a3]" />
        </div>
        <div className="space-y-4">
          {activeJobs.length > 0 ? (
            activeJobs.map((job, index) => (
              <ActiveJobItem key={index} job={job} />
            ))
          ) : (
            <div className="text-center py-8">
              <RotateCw className="h-8 w-8 text-[#a3a3a3] mx-auto mb-3" />
              <p className="text-[#a3a3a3]">No active jobs</p>
            </div>
          )}
        </div>
      </Card>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <Card className="p-6 bg-[#242424] border-[#333333]">
          <div className="flex items-center justify-between mb-6">
            <div>
              <h2 className="text-xl font-semibold">Job Queue</h2>
              <p className="text-sm text-[#a3a3a3] mt-1">Waiting to be processed</p>
            </div>
            <Clock className="h-5 w-5 text-[#a3a3a3]" />
          </div>
          <div className="space-y-4">
            {queuedJobs.map((job, index) => (
              <QueuedJobItem key={index} job={job} />
            ))}
          </div>
        </Card>

        <Card className="p-6 bg-[#242424] border-[#333333]">
          <div className="flex items-center justify-between mb-6">
            <div>
              <h2 className="text-xl font-semibold">Completed Jobs</h2>
              <p className="text-sm text-[#a3a3a3] mt-1">Recently finished</p>
            </div>
            <CheckCircle className="h-5 w-5 text-[#a3a3a3]" />
          </div>
          <div className="space-y-4">
            {completedJobs.map((job, index) => (
              <CompletedJobItem key={index} job={job} />
            ))}
          </div>
        </Card>
      </div>

      <Card className="p-6 bg-[#242424] border-[#333333]">
        <div className="flex items-center justify-between mb-6">
          <div>
            <h2 className="text-xl font-semibold">Processing Log</h2>
            <p className="text-sm text-[#a3a3a3] mt-1">Recent activity and events</p>
          </div>
          <FileText className="h-5 w-5 text-[#a3a3a3]" />
        </div>
        <div className="space-y-4">
          <LogEntry 
            type="info"
            message="Started processing batch_001"
            timestamp="2 minutes ago"
          />
          <LogEntry 
            type="success"
            message="Successfully completed processing of 24 files"
            timestamp="5 minutes ago"
          />
          <LogEntry 
            type="warning"
            message="High memory usage detected"
            timestamp="10 minutes ago"
          />
        </div>
      </Card>
    </div>
  );
};

const StatCard = ({ icon, label, value }: { icon: React.ReactNode; label: string; value: number | string }) => (
  <Card className="p-6 bg-[#242424] border-[#333333]">
    <div className="flex items-center space-x-4">
      <div className="p-3 bg-[#2d2d2d] rounded-lg">{icon}</div>
      <div>
        <p className="text-[#a3a3a3] text-sm">{label}</p>
        <p className="text-2xl font-bold mt-1">{value}</p>
      </div>
    </div>
  </Card>
);

const ActiveJobItem = ({ job }: { job: any }) => (
  <div className="bg-[#2d2d2d] rounded-lg p-4">
    <div className="flex items-center justify-between mb-3">
      <div className="flex items-center space-x-3">
        <Activity className="h-5 w-5 text-[#ff6b2b]" />
        <h3 className="font-medium">Processing {job.name || 'batch_001'}</h3>
      </div>
      <Button variant="outline" size="sm" className="border-[#333333]">
        Cancel
      </Button>
    </div>
    <div className="space-y-2">
      <div className="flex items-center justify-between text-sm">
        <span className="text-[#a3a3a3]">Progress</span>
        <span>{job.progress || '45%'}</span>
      </div>
      <div className="h-2 bg-[#242424] rounded-full">
        <div 
          className="h-full bg-[#ff6b2b] rounded-full"
          style={{ width: job.progress || '45%' }}
        />
      </div>
      <div className="flex justify-between text-sm text-[#a3a3a3]">
        <span>{job.filesProcessed || '11/24 files'}</span>
        <span>{job.remaining || 'Est. 2 min remaining'}</span>
      </div>
    </div>
  </div>
);

const QueuedJobItem = ({ job }: { job: any }) => (
  <div className="bg-[#2d2d2d] rounded-lg p-4">
    <h3 className="font-medium">{job.name || 'Queued Job'}</h3>
  </div>
);

const CompletedJobItem = ({ job }: { job: any }) => (
  <div className="bg-[#2d2d2d] rounded-lg p-4">
    <h3 className="font-medium">{job.name || 'Completed Job'}</h3>
  </div>
);

const LogEntry = ({ type, message, timestamp }: { type: string; message: string; timestamp: string }) => (
  <div className="flex items-center space-x-4">
    <div className="w-2 h-2 rounded-full" style={{ backgroundColor: type === 'success' ? 'green' : type === 'warning' ? 'orange' : 'blue' }} />
    <div>
      <p className="text-sm">{message}</p>
      <p className="text-xs text-[#a3a3a3]">{timestamp}</p>
    </div>
  </div>
);

export default ProcessingDashboard;
