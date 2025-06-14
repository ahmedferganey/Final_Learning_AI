import React, { useEffect, useRef } from 'react';

function VideoPlayer({ metadata }) {
  const videoRef = useRef();
  const canvasRef = useRef();

  useEffect(() => {
    const drawBoxes = () => {
      const canvas = canvasRef.current;
      const ctx = canvas.getContext("2d");
      const img = videoRef.current;

      canvas.width = img.width;
      canvas.height = img.height;

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      metadata?.detections?.forEach(det => {
        const [x, y, w, h] = det.bbox;
        ctx.strokeStyle = det.violation ? 'red' : 'lime';
        ctx.lineWidth = 2;
        ctx.strokeRect(x, y, w, h);
        ctx.fillText(det.label, x, y - 5);
      });

      requestAnimationFrame(drawBoxes);
    };

    const img = videoRef.current;
    img.onload = () => drawBoxes();
  }, [metadata]);

  return (
    <div style={{ position: 'relative', width: '640px' }}>
      <img ref={videoRef} src="http://localhost:8000/video" alt="Stream" style={{ width: '100%' }} />
      <canvas ref={canvasRef} style={{ position: 'absolute', top: 0, left: 0 }} />
    </div>
  );
}

export default VideoPlayer;

