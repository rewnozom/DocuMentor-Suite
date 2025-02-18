import React from "react";

interface ProgressProps {
  value: number;
  className?: string;
}

const Progress: React.FC<ProgressProps> = ({ value, className = "" }) => {
  return (
    <div className={`w-full bg-gray-300 rounded-full h-2 ${className}`}>
      <div
        style={{ width: `${value}%` }}
        className="bg-blue-500 h-full rounded-full"
      />
    </div>
  );
};

export { Progress };
