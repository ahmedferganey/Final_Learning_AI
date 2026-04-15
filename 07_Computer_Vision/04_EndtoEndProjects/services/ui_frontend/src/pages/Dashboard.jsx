import React from "react";
import { Helmet } from "react-helmet-async";

const Dashboard = () => {
  return (
    <>
      <Helmet>
        <title>Dashboard | Pizza Store App</title>
        <meta name="description" content="Manage your dashboard and view insights here." />
        <meta property="og:title" content="Dashboard | Pizza Store App" />
      </Helmet>

      <div className="p-8 bg-gray-100 dark:bg-gray-800 rounded-lg shadow">
        <h2 className="text-xl font-bold text-gray-900 dark:text-white">
          Welcome to the Dashboard
        </h2>
        <p className="mt-2 text-gray-700 dark:text-gray-300">
          This changes based on the theme.
        </p>
      </div>
    </>
  );
};

export default Dashboard;

