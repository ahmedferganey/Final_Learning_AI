import logo from './logo.svg';
import './App.css';
import React from 'react';
import VideoStream from './components/VideoStream';
import ViolationStats from './components/ViolationStats';
import AlertsPanel from './components/AlertsPanel';


function App() {
  return (
    <div className="App">
      <h1>🍕 Pizza Violation Monitoring</h1>
      <VideoStream />
      <ViolationStats />
      <AlertsPanel />
    </div>
  );
}

export default App;
