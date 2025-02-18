import React, { ReactNode } from "react";

interface AlertProps {
  children: ReactNode;
  className?: string;
}

const Alert: React.FC<AlertProps> = ({ children, className = "" }) => {
  return (
    <div
      className={`flex items-center space-x-2 p-4 border rounded-lg bg-red-50 text-red-700 ${className}`}
    >
      {children}
    </div>
  );
};

interface AlertTitleProps {
  children: ReactNode;
  className?: string;
}

const AlertTitle: React.FC<AlertTitleProps> = ({ children, className = "" }) => {
  return <h4 className={`font-bold ${className}`}>{children}</h4>;
};

interface AlertDescriptionProps {
  children: ReactNode;
  className?: string;
}

const AlertDescription: React.FC<AlertDescriptionProps> = ({
  children,
  className = "",
}) => {
  return <p className={`${className}`}>{children}</p>;
};

export { Alert, AlertTitle, AlertDescription };
