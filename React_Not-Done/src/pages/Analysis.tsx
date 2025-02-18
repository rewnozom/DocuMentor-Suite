// src/pages/Analysis.tsx
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useApiContext } from '../api';
import { useToast } from "../components/ui/use-toast";
import { Card } from "../components/ui/card";
import { Button } from "../components/ui/Button";
import { Alert, AlertDescription } from "../components/ui/Alert";
import { 
  Upload,
  FolderOpen,
  FileText,
  Settings,
  AlertCircle,
  X,
  CheckCircle
} from 'lucide-react';

const Analysis = () => {
  // Använd non-null assertion för att försäkra att kontexten inte är null.
  const { files: apiFiles, analysis } = useApiContext()!;
  const { toast } = useToast();
  const navigate = useNavigate();

  const [files, setFiles] = useState<File[]>([]);
  const [uploadedFiles, setUploadedFiles] = useState<any[]>([]);
  const [dragActive, setDragActive] = useState(false);
  const [selectedCommands, setSelectedCommands] = useState({
    f: true,
    s: false,
    t: false,
    c: false
  });
  const [processing, setProcessing] = useState(false);

  const validateFile = (file: File) => {
    const validTypes = ['.md', '.txt'];
    const extension = file.name.substring(file.name.lastIndexOf('.')).toLowerCase();
    return validTypes.includes(extension);
  };

  const handleDrag = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === 'dragenter' || e.type === 'dragover') {
      setDragActive(true);
    } else {
      setDragActive(false);
    }
  };

  const handleDrop = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);

    const droppedFiles = Array.from(e.dataTransfer.files);
    const validFiles = droppedFiles.filter(validateFile);
    setFiles((prev) => [...prev, ...validFiles]);
  };

  const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFiles = e.target.files ? Array.from(e.target.files) : [];
    const validFiles = selectedFiles.filter(validateFile);
    setFiles((prev) => [...prev, ...validFiles]);
  };

  const removeFile = (index: number) => {
    setFiles((prev) => prev.filter((_, i) => i !== index));
  };

  // Funktion för att ladda upp filer via API
  const uploadFiles = async () => {
    if (files.length === 0) return;
    try {
      setProcessing(true);
      const result = await apiFiles.uploadFiles(files);
      setUploadedFiles(result.files);
      toast({
        title: "Files uploaded successfully",
        description: `${result.files.length} files ready for analysis`,
        variant: "success"
      });
    } catch (error: any) {
      toast({
        title: "Upload failed",
        description: error.message,
        variant: "destructive"
      });
    } finally {
      setProcessing(false);
    }
  };

  // Starta analys – laddar upp filer om de inte redan är uppladdade
  const startAnalysis = async () => {
    try {
      setProcessing(true);
      let uploaded = uploadedFiles;
      if (!uploaded.length && files.length > 0) {
        const result = await apiFiles.uploadFiles(files);
        uploaded = result.files;
        setUploadedFiles(uploaded);
        toast({
          title: "Files uploaded successfully",
          description: `${uploaded.length} files ready for analysis`,
          variant: "success"
        });
      }
      if (!uploaded.length) {
        toast({
          title: "No files to process",
          description: "Please upload some files before starting analysis",
          variant: "destructive"
        });
        return;
      }
      const config = {
        commands: Object.entries(selectedCommands)
          .filter(([_, enabled]) => enabled)
          .map(([cmd]) => cmd),
        files: uploaded.map((f) => f.id) // förväntar att varje uppladdad fil har en "id"
      };

      const job = await analysis.startAnalysis(config);
      toast({
        title: "Analysis started",
        description: `Job ID: ${job.id}`,
        variant: "success"
      });
      navigate(`/processing/${job.id}`);
    } catch (error: any) {
      toast({
        title: "Failed to start analysis",
        description: error.message,
        variant: "destructive"
      });
    } finally {
      setProcessing(false);
    }
  };

  return (
    <div className="space-y-8">
      {/* Header */}
      <div>
        <h1 className="text-3xl font-bold mb-2">Analysis Configuration</h1>
        <p className="text-[#a3a3a3]">Configure and prepare files for processing</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* File Upload Section */}
        <div className="lg:col-span-2 space-y-6">
          <Card className="p-6 bg-[#242424] border-[#333333]">
            <div className="flex items-center justify-between mb-6">
              <h2 className="text-xl font-semibold">Upload Files</h2>
              <Upload className="h-5 w-5 text-[#a3a3a3]" />
            </div>
            
            <div 
              className={`border-2 border-dashed rounded-lg p-8 text-center transition-colors duration-200 ${dragActive ? 'border-[#ff6b2b] bg-[#ff6b2b]/10' : 'border-[#333333]'}`}
              onDragEnter={handleDrag}
              onDragLeave={handleDrag}
              onDragOver={handleDrag}
              onDrop={handleDrop}
            >
              <FolderOpen className="mx-auto h-12 w-12 text-[#ff6b2b] mb-4" />
              <div className="space-y-4">
                <h3 className="text-lg font-medium">Drag & Drop Files</h3>
                <p className="text-[#a3a3a3]">or</p>
                <Button 
                  variant="default" 
                  className="bg-[#ff6b2b] hover:bg-[#ff8c58]"
                  onClick={() => document.getElementById('file-upload')?.click()}
                >
                  Browse Files
                </Button>
                <input
                  id="file-upload"
                  type="file"
                  multiple
                  accept=".md,.txt"
                  className="hidden"
                  onChange={handleFileSelect}
                />
                <p className="text-sm text-[#a3a3a3]">
                  Supported formats: .md, .txt
                </p>
              </div>
            </div>
          </Card>

          {/* File List */}
          <Card className="p-6 bg-[#242424] border-[#333333]">
            <div className="flex items-center justify-between mb-6">
              <h2 className="text-xl font-semibold">Selected Files</h2>
              <FileText className="h-5 w-5 text-[#a3a3a3]" />
            </div>
            
            {files.length > 0 ? (
              <div className="space-y-4">
                {files.map((file, index) => (
                  <FileItem 
                    key={index}
                    file={file}
                    onRemove={() => removeFile(index)}
                  />
                ))}
              </div>
            ) : (
              <Alert>
                <AlertCircle className="h-4 w-4" />
                <AlertDescription>
                  No files selected. Upload files to begin analysis.
                </AlertDescription>
              </Alert>
            )}
          </Card>
        </div>

        {/* Configuration Section */}
        <div className="space-y-6">
          <Card className="p-6 bg-[#242424] border-[#333333]">
            <div className="flex items-center justify-between mb-6">
              <h2 className="text-xl font-semibold">Commands</h2>
              <Settings className="h-5 w-5 text-[#a3a3a3]" />
            </div>
            
            <div className="space-y-4">
              <CommandToggle
                id="f"
                label="Full Info (-f)"
                description="Complete product information"
                checked={selectedCommands.f}
                onChange={(checked) => 
                  setSelectedCommands(prev => ({ ...prev, f: checked }))
                }
              />
              <CommandToggle
                id="s"
                label="Summary (-s)"
                description="Product summary"
                checked={selectedCommands.s}
                onChange={(checked) =>
                  setSelectedCommands(prev => ({ ...prev, s: checked }))
                }
              />
              <CommandToggle
                id="t"
                label="Technical (-t)"
                description="Technical specifications"
                checked={selectedCommands.t}
                onChange={(checked) =>
                  setSelectedCommands(prev => ({ ...prev, t: checked }))
                }
              />
              <CommandToggle
                id="c"
                label="Compatibility (-c)"
                description="Compatibility information"
                checked={selectedCommands.c}
                onChange={(checked) =>
                  setSelectedCommands(prev => ({ ...prev, c: checked }))
                }
              />
            </div>
          </Card>

          <Card className="p-6 bg-[#242424] border-[#333333]">
            <div className="flex items-center justify-between mb-6">
              <h2 className="text-xl font-semibold">Options</h2>
              <Settings className="h-5 w-5 text-[#a3a3a3]" />
            </div>
            
            <div className="space-y-4">
              <div className="space-y-2">
                <label className="text-sm font-medium">Workers</label>
                <input 
                  type="number" 
                  min="1" 
                  max="8" 
                  defaultValue="4"
                  className="w-full bg-[#2d2d2d] border border-[#333333] rounded-lg px-3 py-2"
                />
              </div>
              <div className="space-y-2">
                <label className="text-sm font-medium">Output Directory</label>
                <div className="flex items-center space-x-2">
                  <input 
                    type="text" 
                    defaultValue="./output"
                    className="flex-1 bg-[#2d2d2d] border border-[#333333] rounded-lg px-3 py-2"
                  />
                  <Button variant="outline" className="border-[#333333]">
                    Browse
                  </Button>
                </div>
              </div>
            </div>
          </Card>

          <Button 
            className="w-full bg-[#ff6b2b] hover:bg-[#ff8c58]"
            disabled={files.length === 0 || processing}
            onClick={startAnalysis}
          >
            {processing ? 'Processing...' : 'Start Analysis'}
          </Button>
        </div>
      </div>
    </div>
  );
};

const FileItem = ({ file, onRemove }: { file: File; onRemove: () => void }) => (
  <div className="flex items-center justify-between p-4 bg-[#2d2d2d] rounded-lg">
    <div className="flex items-center space-x-4">
      <FileText className="h-5 w-5 text-[#ff6b2b]" />
      <div>
        <p className="font-medium">{file.name}</p>
        <p className="text-sm text-[#a3a3a3]">
          {(file.size / 1024).toFixed(1)} KB
        </p>
      </div>
    </div>
    <button 
      onClick={onRemove}
      className="p-1 hover:bg-[#242424] rounded-full transition-colors"
    >
      <X className="h-5 w-5 text-[#a3a3a3]" />
    </button>
  </div>
);

const CommandToggle = ({ id, label, description, checked, onChange }: { 
  id: string; 
  label: string; 
  description: string; 
  checked: boolean; 
  onChange: (checked: boolean) => void 
}) => (
  <div className="flex items-start space-x-3">
    <div className="pt-0.5">
      <input
        type="checkbox"
        id={id}
        checked={checked}
        onChange={(e) => onChange(e.target.checked)}
        className="hidden"
      />
      <div 
        className={`w-5 h-5 rounded border-2 cursor-pointer flex items-center justify-center transition-colors duration-200 ${checked ? 'bg-[#ff6b2b] border-[#ff6b2b]' : 'border-[#333333]'}`}
        onClick={() => onChange(!checked)}
      >
        {checked && <CheckCircle className="h-4 w-4 text-white" />}
      </div>
    </div>
    <div className="flex-1">
      <label htmlFor={id} className="text-sm font-medium cursor-pointer">{label}</label>
      <p className="text-sm text-[#a3a3a3]">{description}</p>
    </div>
  </div>
);

export default Analysis;
