import React, { ReactNode, ButtonHTMLAttributes } from "react";

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "default" | "outline" | "ghost";
  size?: "sm" | "md" | "lg" | "icon";
  children: ReactNode;
  className?: string;
}

const Button: React.FC<ButtonProps> = ({
  variant = "default",
  size = "md",
  children,
  className = "",
  ...props
}) => {
  let baseClasses = "px-4 py-2 rounded transition-colors";
  if (variant === "default") {
    baseClasses += " bg-blue-500 text-white hover:bg-blue-600";
  } else if (variant === "outline") {
    baseClasses += " border border-gray-300 text-gray-700 hover:bg-gray-100";
  } else if (variant === "ghost") {
    baseClasses += " bg-transparent text-gray-700 hover:bg-gray-100";
  }
  if (size === "icon") {
    baseClasses = "p-2";
  }
  return (
    <button className={`${baseClasses} ${className}`} {...props}>
      {children}
    </button>
  );
};

export { Button };
