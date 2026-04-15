// src/features/streaming/WebSocketViewer.jsx
import React from "react";
import useWebSocketFrame from "./useWebSocketFrame";

const WebSocketViewer = () => {
  const env = typeof window !== "undefined" && window._env_
    ? window._env_
    : import.meta.env;

  const wsUrl = env.VITE_WEBSOCKET_URL || `ws://${window.location.hostname}:8000/ws/frames`;
  const frameUrl = useWebSocketFrame(wsUrl);

  return (
    <div className="flex flex-col items-center gap-4">
      <h2 className="text-xl font-semibold text-gray-800 dark:text-white">
        🔴 Live Streaming (WebSocket)
      </h2>
      {frameUrl ? (
        <img
          src={frameUrl}
          alt="Live Stream"
          width={640}
          height="auto"
          className="rounded shadow-lg max-w-full border"
        />
      ) : (
        <p className="text-gray-500 animate-pulse">Waiting for video stream...</p>
      )}
    </div>
  );
};

export default WebSocketViewer;
