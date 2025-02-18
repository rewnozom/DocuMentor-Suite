// src/pages/Dashboard.tsx
import React from 'react';
import { Card } from "../components/ui/card";

import { FileText, Database, Clock, AlertCircle, BarChart, CheckCircle } from 'lucide-react';
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

const Dashboard = () => {
  // Placeholder-data
  const processingStats = {
    filesProcessed: 1247,
    trainingSamples: 4928,
    successRate: 98.5,
    avgProcessingTime: '1.2s'
  };

  const recentActivity = [
    { timestamp: '2024-02-16 14:30', action: 'Processing completed', status: 'success' },
    { timestamp: '2024-02-16 14:15', action: 'Analysis started', status: 'info' },
    { timestamp: '2024-02-16 14:00', action: 'Files uploaded', status: 'info' }
  ];

  return (
    <div className="space-y-8">
      {/* Header */}
      <div>
        <h1 className="text-3xl font-bold mb-2">Dashboard</h1>
        <p className="text-[#a3a3a3]">System overview and statistics</p>
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <StatCard 
          icon={<FileText className="text-[#ff6b2b]" />}
          label="Files Processed"
          value={processingStats.filesProcessed}
        />
        <StatCard 
          icon={<Database className="text-[#ff6b2b]" />}
          label="Training Samples"
          value={processingStats.trainingSamples}
        />
        <StatCard 
          icon={<CheckCircle className="text-[#ff6b2b]" />}
          label="Success Rate"
          value={`${processingStats.successRate}%`}
        />
        <StatCard 
          icon={<Clock className="text-[#ff6b2b]" />}
          label="Avg. Processing Time"
          value={processingStats.avgProcessingTime}
        />
      </div>

      {/* Charts and Activity */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Processing Chart */}
        <Card className="p-6 bg-[#242424] border-[#333333]">
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-xl font-semibold">Processing Activity</h2>
            <BarChart className="h-5 w-5 text-[#a3a3a3]" />
          </div>
          <div className="h-[300px]">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={generateChartData()}>
                <XAxis dataKey="name" stroke="#a3a3a3" />
                <YAxis stroke="#a3a3a3" />
                <Tooltip 
                  contentStyle={{ 
                    backgroundColor: '#2d2d2d',
                    border: 'none',
                    borderRadius: '8px'
                  }}
                />
                <Line 
                  type="monotone" 
                  dataKey="value" 
                  stroke="#ff6b2b" 
                  strokeWidth={2}
                />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </Card>

        {/* Recent Activity */}
        <Card className="p-6 bg-[#242424] border-[#333333]">
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-xl font-semibold">Recent Activity</h2>
            <AlertCircle className="h-5 w-5 text-[#a3a3a3]" />
          </div>
          <div className="space-y-4">
            {recentActivity.map((activity, index) => (
              <ActivityItem key={index} {...activity} />
            ))}
          </div>
        </Card>
      </div>

      {/* System Status */}
      <Card className="p-6 bg-[#242424] border-[#333333]">
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-xl font-semibold">System Status</h2>
          <AlertCircle className="h-5 w-5 text-[#a3a3a3]" />
        </div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <StatusItem 
            label="Backend Connection" 
            status="connected"
            details="Latency: 42ms"
          />
          <StatusItem 
            label="Processing Queue" 
            status="operational"
            details="0 pending tasks"
          />
          <StatusItem 
            label="Training Pipeline" 
            status="operational"
            details="Ready for processing"
          />
        </div>
      </Card>
    </div>
  );
};

const StatCard = ({ icon, label, value }: { icon: React.ReactNode; label: string; value: number | string }) => (
  <Card className="p-6 bg-[#242424] border-[#333333]">
    <div className="flex items-center space-x-4">
      <div className="p-3 bg-[#2d2d2d] rounded-lg">
        {icon}
      </div>
      <div>
        <p className="text-[#a3a3a3] text-sm">{label}</p>
        <p className="text-2xl font-bold mt-1">{value}</p>
      </div>
    </div>
  </Card>
);

const ActivityItem = ({ timestamp, action, status }: { timestamp: string; action: string; status: string }) => (
  <div className="flex items-center space-x-4">
    <div className={`w-2 h-2 rounded-full ${status === 'success' ? 'bg-green-500' : 'bg-blue-500'}`} />
    <div>
      <p className="text-sm">{action}</p>
      <p className="text-xs text-[#a3a3a3]">{timestamp}</p>
    </div>
  </div>
);

const StatusItem = ({ label, status, details }: { label: string; status: string; details: string }) => (
  <div className="flex items-center space-x-4">
    <div className={`w-3 h-3 rounded-full ${status === 'connected' ? 'bg-green-500' : 'bg-blue-500'}`} />
    <div>
      <p className="font-medium">{label}</p>
      <p className="text-sm text-[#a3a3a3]">{details}</p>
    </div>
  </div>
);

const generateChartData = () => {
  return Array.from({ length: 7 }, (_, i) => ({
    name: `Day ${i + 1}`,
    value: Math.floor(Math.random() * 100) + 50
  }));
};

export default Dashboard;
