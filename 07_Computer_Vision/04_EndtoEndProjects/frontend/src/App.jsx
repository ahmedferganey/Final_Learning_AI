import React, { useEffect, useState } from 'react';
import VideoPlayer from './components/VideoPlayer';
import MetadataPanel from './components/MetadataPanel';

function App() {
  const [metadata, setMetadata] = useState({});

  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8000/ws");

    ws.onmessage = () => {
      fetch("http://localhost:8000/metadata")
        .then(res => res.json())
        .then(setMetadata);
    };

    return () => ws.close();
  }, []);

  return (
    <div>
      <h1>🍕 Pizza Store Monitor</h1>
      <VideoPlayer metadata={metadata} />
      <MetadataPanel metadata={metadata} />
    </div>
  );
}

export default App;

