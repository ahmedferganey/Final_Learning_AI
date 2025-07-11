import React from "react";
import { Helmet } from "react-helmet-async";

const Reports = () => (
  <>
    <Helmet>
      <title>Reports | Pizza Store App</title>
      <meta name="description" content="View reports and analytics about orders and performance." />
      <meta property="og:title" content="Reports | Pizza Store App" />
    </Helmet>

    <h1 className="text-2xl text-gray-800 dark:text-white">Reports</h1>
  </>
);

export default Reports;

