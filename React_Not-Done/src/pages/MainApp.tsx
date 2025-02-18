// src/pages/MainApp.tsx
import React, { useState } from 'react';
import { Card } from "../components/ui/card";
import { Button } from "../components/ui/Button";
import { Alert, AlertDescription, AlertTitle } from "../components/ui/Alert";
import { CardContent, CardHeader, CardTitle } from "../components/ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "../components/ui/Tabs";
import { FolderOpen, Settings2, FileText, Database, AlertCircle, ChevronRight, Code } from 'lucide-react';

const MainApp = () => {
  const [activeSection, setActiveSection] = useState('input');
  const [processing, setProcessing] = useState(false);
  const [results, setResults] = useState<any>(null);

  return (
    <div className="min-h-screen bg-gray-100 dark:bg-gray-900">
      {/* Header */}
      <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
        <div className="container flex h-14 items-center">
          <div className="mr-4 flex">
            <a className="mr-6 flex items-center space-x-2" href="/">
              <Code className="h-6 w-6" />
              <span className="font-bold">Markdown Analyzer</span>
            </a>
          </div>
          <div className="flex flex-1 items-center justify-between space-x-2 md:justify-end">
            <Button variant="ghost" size="icon">
              <Settings2 className="h-4 w-4" />
            </Button>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="container mx-auto py-6">
        <div className="grid gap-6 lg:grid-cols-12">
          {/* Sidebar */}
          <div className="lg:col-span-3">
            <Card>
              <CardHeader>
                <CardTitle>Navigation</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-2">
                  <Button 
                    variant={activeSection === 'input' ? "default" : "ghost"} 
                    className="w-full justify-start"
                    onClick={() => setActiveSection('input')}
                  >
                    <FolderOpen className="mr-2 h-4 w-4" />
                    Input Files
                  </Button>
                  <Button 
                    variant={activeSection === 'process' ? "default" : "ghost"}
                    className="w-full justify-start"
                    onClick={() => setActiveSection('process')}
                  >
                    <FileText className="mr-2 h-4 w-4" />
                    Processing
                  </Button>
                  <Button 
                    variant={activeSection === 'results' ? "default" : "ghost"}
                    className="w-full justify-start"
                    onClick={() => setActiveSection('results')}
                  >
                    <Database className="mr-2 h-4 w-4" />
                    Results
                  </Button>
                </div>
              </CardContent>
            </Card>
          </div>

          {/* Main Content Area */}
          <div className="lg:col-span-9">
            <Tabs defaultValue={activeSection}>
              <TabsContent value="input" className="space-y-4">
                <InputSection onFilesSelected={(files) => console.log('Files:', files)} />
              </TabsContent>
              <TabsContent value="process" className="space-y-4">
                <ProcessingSection processing={processing} />
              </TabsContent>
              <TabsContent value="results" className="space-y-4">
                <ResultsSection results={results} />
              </TabsContent>
            </Tabs>
          </div>
        </div>
      </main>
    </div>
  );
};

const InputSection = ({ onFilesSelected }: { onFilesSelected: (files: File[]) => void }) => {
  return (
    <div className="space-y-4">
      <Card>
        <CardHeader>
          <CardTitle>Select Input Files</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid gap-4">
            <div className="border-2 border-dashed rounded-lg p-6 text-center">
              <FolderOpen className="mx-auto h-8 w-8 mb-4" />
              <div className="space-y-2">
                <Button>Choose Files</Button>
                <p className="text-sm text-muted-foreground">
                  or drag and drop your files here
                </p>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>
      <Card>
        <CardHeader>
          <CardTitle>Selected Files</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-2">
            <Alert>
              <AlertCircle className="h-4 w-4" />
              <AlertTitle>No files selected</AlertTitle>
              <AlertDescription>
                Please select files to begin processing
              </AlertDescription>
            </Alert>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

const ProcessingSection = ({ processing }: { processing: boolean }) => {
  return (
    <div className="space-y-4">
      <Card>
        <CardHeader>
          <CardTitle>Processing Configuration</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid gap-4">
            <CommandSelector />
            <ProcessingOptions />
          </div>
        </CardContent>
      </Card>
      <Card>
        <CardHeader>
          <CardTitle>Processing Status</CardTitle>
        </CardHeader>
        <CardContent>
          {processing ? (
            <ProcessingStatus />
          ) : (
            <Alert>
              <AlertCircle className="h-4 w-4" />
              <AlertTitle>Ready to Process</AlertTitle>
              <AlertDescription>
                Configure your settings and click Start Processing
              </AlertDescription>
            </Alert>
          )}
        </CardContent>
      </Card>
    </div>
  );
};

const ResultsSection = ({ results }: { results: any }) => {
  return (
    <div className="space-y-4">
      <Card>
        <CardHeader>
          <CardTitle>Processing Results</CardTitle>
        </CardHeader>
        <CardContent>
          {results ? (
            <ResultsSummary results={results} />
          ) : (
            <Alert>
              <AlertCircle className="h-4 w-4" />
              <AlertTitle>No Results Available</AlertTitle>
              <AlertDescription>
                Start processing to see results
              </AlertDescription>
            </Alert>
          )}
        </CardContent>
      </Card>
    </div>
  );
};

// Helper Components
const CommandSelector = () => {
  const commands = [
    { id: 'f', name: 'Full Info (-f)', description: 'Complete product information' },
    { id: 's', name: 'Summary (-s)', description: 'Product summary' },
    { id: 't', name: 'Technical (-t)', description: 'Technical specifications' },
    { id: 'c', name: 'Compatibility (-c)', description: 'Compatibility information' }
  ];

  return (
    <div className="space-y-4">
      <h3 className="text-lg font-medium">Select Commands</h3>
      <div className="grid gap-2">
        {commands.map((command) => (
          <div key={command.id} className="flex items-center space-x-2">
            <input type="checkbox" id={command.id} className="h-4 w-4" />
            <label htmlFor={command.id} className="text-sm font-medium">
              {command.name}
              <p className="text-sm text-muted-foreground">{command.description}</p>
            </label>
          </div>
        ))}
      </div>
    </div>
  );
};

const ProcessingOptions = () => {
  return (
    <div className="space-y-4">
      <h3 className="text-lg font-medium">Processing Options</h3>
      <div className="grid gap-4">
        <div className="space-y-2">
          <label className="text-sm font-medium">Number of Workers</label>
          <input type="number" className="w-full rounded-md border px-3 py-2" min="1" max="8" defaultValue="4" />
        </div>
        <div className="space-y-2">
          <label className="text-sm font-medium">Output Directory</label>
          <div className="flex items-center space-x-2">
            <input type="text" className="flex-1 rounded-md border px-3 py-2" defaultValue="./output" />
            <Button variant="outline">Browse</Button>
          </div>
        </div>
      </div>
    </div>
  );
};

const ProcessingStatus = () => {
  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <span className="text-sm font-medium">Processing Files...</span>
        <span className="text-sm text-muted-foreground">50%</span>
      </div>
      <div className="h-2 rounded-full bg-muted">
        <div className="h-full w-1/2 rounded-full bg-primary"></div>
      </div>
      <div className="space-y-2">
        <div className="flex items-center text-sm">
          <ChevronRight className="h-4 w-4 mr-2" />
          Processing document_1.md...
        </div>
      </div>
    </div>
  );
};

const ResultsSummary = ({ results }: { results: any }) => {
  return (
    <div className="space-y-6">
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <ResultCard title="Files Processed" value="24" />
        <ResultCard title="Training Examples" value="96" />
        <ResultCard title="Success Rate" value="98%" />
        <ResultCard title="Processing Time" value="1m 24s" />
      </div>
      
      <div className="space-y-4">
        <h3 className="text-lg font-medium">Generated Files</h3>
        <div className="space-y-2">
          {/* File list would go here */}
        </div>
      </div>
    </div>
  );
};

const ResultCard = ({ title, value }: { title: string; value: string }) => {
  return (
    <Card>
      <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
        <CardTitle className="text-sm font-medium">{title}</CardTitle>
      </CardHeader>
      <div className="p-4">
        <div className="text-2xl font-bold">{value}</div>
      </div>
    </Card>
  );
};

export default MainApp;
