import React from "react";
import { Helmet } from "react-helmet-async";

const Detection = () => (
  <>
    <Helmet>
      <title>Detection | Pizza Store App</title>
      <meta name="description" content="Real-time detection for quality control in our kitchen." />
      <meta property="og:title" content="Detection | Pizza Store App" />
    </Helmet>

    <h1 className="text-2xl text-gray-800 dark:text-white">Detection</h1>
  </>
);

export default Detection;

