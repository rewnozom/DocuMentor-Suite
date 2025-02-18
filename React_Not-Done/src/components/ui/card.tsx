import React, { ReactNode } from "react";

interface CardProps {
  children: ReactNode;
  className?: string;
}

const Card: React.FC<CardProps> = ({ children, className = "" }) => {
  return <div className={`rounded-lg shadow p-4 ${className}`}>{children}</div>;
};

const CardHeader: React.FC<CardProps> = ({ children, className = "" }) => {
  return <div className={`border-b pb-2 ${className}`}>{children}</div>;
};

const CardContent: React.FC<CardProps> = ({ children, className = "" }) => {
  return <div className={`py-2 ${className}`}>{children}</div>;
};

const CardTitle: React.FC<CardProps> = ({ children, className = "" }) => {
  return <h2 className={`text-xl font-bold ${className}`}>{children}</h2>;
};

export { Card, CardHeader, CardContent, CardTitle };
