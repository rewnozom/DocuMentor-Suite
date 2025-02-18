// src/pages/Settings.tsx
import React from 'react';
import { Card } from "../components/ui/card";

const Settings = () => {
  return (
    <div className="space-y-8">
      <Card className="p-6 bg-[#242424] border-[#333333]">
        <h2 className="text-xl font-semibold">Settings</h2>
        <p className="text-[#a3a3a3]">Settings page content goes here.</p>
      </Card>
    </div>
  );
};

export default Settings;
