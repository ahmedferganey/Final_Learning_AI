// src/features/streaming/WebSocketViewer.jsx
import React from "react";
import { useWebSocketFrame } from "./useWebSocketFrame";

const WebSocketViewer = () => {
  const { frameURL } = useWebSocketFrame();

  return (
    <div className="flex flex-col items-center gap-4">
      <h2 className="text-xl font-semibold text-gray-800 dark:text-white">
        Live Stream (WebSocket)
      </h2>
      {frameURL ? (
        <img
          src={frameURL}
          alt="Live Frame"
          className="rounded shadow-lg max-w-full border"
        />
      ) : (
        <p className="text-gray-500">Waiting for frames...</p>
      )}
    </div>
  );
};

export default WebSocketViewer;

