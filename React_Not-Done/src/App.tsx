// src/App.tsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route, NavLink } from 'react-router-dom';
import { ApiProvider } from './api';
import { Toaster } from './components/ui/toaster';
import { Home, FileText, Activity, Database, Settings, BarChart2 } from 'lucide-react';

// Sidor
import Dashboard from './pages/Dashboard';
import Analysis from './pages/Analysis';
import ProcessingDashboard from './pages/ProcessingDashboard';
import ProcessingDetail from './pages/ProcessingDetail';
import Results from './pages/Results';
import SettingsPage from './pages/Settings';

const App = () => {
  return (
    <ApiProvider>
      <Router>
        <div className="min-h-screen bg-[#1a1a1a] text-white">
          {/* Sidebar */}
          <nav className="fixed left-0 top-0 h-full w-64 bg-[#242424] border-r border-[#333333] p-6">
            <div className="flex items-center space-x-3 mb-8">
              <BarChart2 className="h-8 w-8 text-[#ff6b2b]" />
              <span className="text-xl font-bold">Analyzer</span>
            </div>
            <div className="space-y-2">
              <NavItem icon={<Home />} to="/" label="Dashboard" />
              <NavItem icon={<FileText />} to="/analysis" label="Analysis" />
              <NavItem icon={<Activity />} to="/processing" label="Processing" />
              <NavItem icon={<Database />} to="/results" label="Results" />
              <NavItem icon={<Settings />} to="/settings" label="Settings" />
            </div>
          </nav>

          {/* Main Content */}
          <main className="ml-64 p-8">
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/analysis" element={<Analysis />} />
              {/* Två routes för Processing: en översikt och en detaljerad vy */}
              <Route path="/processing" element={<ProcessingDashboard />} />
              <Route path="/processing/:jobId" element={<ProcessingDetail />} />
              <Route path="/results" element={<Results />} />
              <Route path="/settings" element={<SettingsPage />} />
            </Routes>
          </main>
          <Toaster />
        </div>
      </Router>
    </ApiProvider>
  );
};

const NavItem = ({ icon, to, label }: { icon: React.ReactNode; to: string; label: string }) => (
  <NavLink
    to={to}
    className={({ isActive }) =>
      `flex items-center space-x-3 px-4 py-3 rounded-lg transition-colors duration-200 ${
        isActive
          ? 'bg-[#2d2d2d] text-[#ff6b2b]'
          : 'text-[#a3a3a3] hover:bg-[#2d2d2d] hover:text-white'
      }`
    }
  >
    {icon}
    <span>{label}</span>
  </NavLink>
);

export default App;
