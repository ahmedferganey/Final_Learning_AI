import React, { useEffect, useRef } from 'react';

import { connectSocket } from '../services/socket';

function VideoStream() {
  const imgRef = useRef(null);

  useEffect(() => {
    const socket = connectSocket();
    socket.binaryType = 'blob';

    socket.onmessage = (event) => {
      const blob = new Blob([event.data], { type: 'image/jpeg' });
      const url = URL.createObjectURL(blob);
      if (imgRef.current) {
        imgRef.current.src = url;
      }
    };

    socket.onerror = (err) => {
      console.error('[WebSocket Error]', err);
    };

    return () => {
      socket.close();
    };
  }, []);

  return (
    <div>
      <h2>🎥 Live Stream</h2>
      <img ref={imgRef} alt="Live video" style={{ width: '640px', border: '2px solid #ccc' }} />
    </div>
  );
}

export default VideoStream;

