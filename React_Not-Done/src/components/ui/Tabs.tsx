import React, {
    useState,
    createContext,
    useContext,
    ReactNode,
  } from "react";
  
  interface TabsContextValue {
    activeTab: string;
    setActiveTab: (tab: string) => void;
  }
  
  const TabsContext = createContext<TabsContextValue | undefined>(undefined);
  
  interface TabsProps {
    defaultValue: string;
    children: ReactNode;
  }
  
  const Tabs: React.FC<TabsProps> = ({ defaultValue, children }) => {
    const [activeTab, setActiveTab] = useState(defaultValue);
    return (
      <TabsContext.Provider value={{ activeTab, setActiveTab }}>
        <div>{children}</div>
      </TabsContext.Provider>
    );
  };
  
  interface TabsListProps {
    children: ReactNode;
    className?: string;
  }
  
  const TabsList: React.FC<TabsListProps> = ({ children, className = "" }) => {
    return <div className={`flex space-x-2 ${className}`}>{children}</div>;
  };
  
  interface TabsTriggerProps {
    value: string;
    children: ReactNode;
    className?: string;
  }
  
  const TabsTrigger: React.FC<TabsTriggerProps> = ({
    value,
    children,
    className = "",
  }) => {
    const context = useContext(TabsContext);
    if (!context) {
      throw new Error("TabsTrigger must be used within a Tabs");
    }
    const { activeTab, setActiveTab } = context;
    return (
      <button
        className={`px-4 py-2 rounded ${
          activeTab === value
            ? "bg-blue-500 text-white"
            : "bg-gray-200 text-gray-700"
        } ${className}`}
        onClick={() => setActiveTab(value)}
      >
        {children}
      </button>
    );
  };
  
  interface TabsContentProps {
    value: string;
    children: ReactNode;
    className?: string;
  }
  
  const TabsContent: React.FC<TabsContentProps> = ({
    value,
    children,
    className = "",
  }) => {
    const context = useContext(TabsContext);
    if (!context) {
      throw new Error("TabsContent must be used within a Tabs");
    }
    const { activeTab } = context;
    return activeTab === value ? <div className={className}>{children}</div> : null;
  };
  
  export { Tabs, TabsList, TabsTrigger, TabsContent };
  