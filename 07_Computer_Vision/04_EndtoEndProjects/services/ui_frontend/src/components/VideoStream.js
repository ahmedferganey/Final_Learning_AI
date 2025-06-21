import React, { useEffect, useRef } from 'react';
import { connectSocket } from '../services/socket';

const VideoStream = () => {
  const canvasRef = useRef(null);

  useEffect(() => {
    const socket = connectSocket();
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');

    socket.onmessage = (event) => {
      const blob = new Blob([event.data], { type: 'image/jpeg' });
      const img = new Image();
      img.onload = () => {
        ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
      };
      img.src = URL.createObjectURL(blob);
    };

    return () => socket.close();
  }, []);

  return (
    <div>
      <h2>Live Video</h2>
      <canvas ref={canvasRef} width="640" height="480" />
    </div>
  );
};

export default VideoStream;

