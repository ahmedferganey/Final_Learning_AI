// src/features/streaming/useWebSocketFrame.js
import { useEffect, useState, useRef } from "react";

const useWebSocketFrame = (wsUrl) => {
  const [frameUrl, setFrameUrl] = useState(null);
  const latestUrl = useRef(null);

  useEffect(() => {
    const socket = new WebSocket(wsUrl);
    socket.binaryType = "arraybuffer";

    socket.onmessage = (event) => {
      const blob = new Blob([event.data], { type: "image/jpeg" });
      const url = URL.createObjectURL(blob);

      setFrameUrl((prevUrl) => {
        if (latestUrl.current) URL.revokeObjectURL(latestUrl.current);
        latestUrl.current = url;
        return url;
      });
    };

    socket.onerror = (err) => console.error("WebSocket Error:", err);

    return () => {
      socket.close();
      if (latestUrl.current) URL.revokeObjectURL(latestUrl.current);
    };
  }, [wsUrl]);

  return frameUrl;
};

export default useWebSocketFrame;

