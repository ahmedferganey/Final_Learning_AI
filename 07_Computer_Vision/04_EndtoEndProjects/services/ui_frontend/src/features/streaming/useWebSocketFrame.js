import { useEffect, useState, useRef } from "react";

// Remove static import of wsURL since now dynamic
// import { wsURL as defaultWS } from "../../utils/config";

export const useWebSocketFrame = (url) => {
  // Use runtime env or fallback to hardcoded default
  const defaultWS = (typeof window !== "undefined" && window._env_?.VITE_WEBSOCKET_URL) || "ws://localhost:9000/ws";
  const [frameURL, setFrameURL] = useState(null);
  const ws = useRef(null);

  useEffect(() => {
    const wsUrl = url || defaultWS;

    if (!wsUrl) {
      console.error("WebSocket URL is not defined.");
      return;
    }

    ws.current = new WebSocket(wsUrl);
    ws.current.binaryType = "arraybuffer";

    ws.current.onmessage = (event) => {
      const blob = new Blob([event.data], { type: "image/jpeg" });
      const objectUrl = URL.createObjectURL(blob);
      setFrameURL((prev) => {
        if (prev) URL.revokeObjectURL(prev);
        return objectUrl;
      });
    };

    ws.current.onerror = (err) => {
      console.error("WebSocket error:", err);
    };

    return () => {
      if (ws.current) ws.current.close();
      setFrameURL((prev) => {
        if (prev) URL.revokeObjectURL(prev);
        return null;
      });
    };
  }, [url, defaultWS]);

  return { frameURL };
};

