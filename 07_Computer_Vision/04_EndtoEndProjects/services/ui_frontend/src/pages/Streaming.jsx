import React from "react";
import { Helmet } from "react-helmet-async";
import WebSocketViewer from "../features/streaming/WebSocketViewer";

const Streaming = () => (
  <>
    <Helmet>
      <title>Live Streaming | Pizza Store App</title>
      <meta name="description" content="Watch live pizza preparation in our kitchen!" />
      <meta property="og:title" content="Live Streaming | Pizza Store App" />
    </Helmet>

    <div className="text-center p-4">
      <WebSocketViewer />
    </div>
  </>
);

export default Streaming;

