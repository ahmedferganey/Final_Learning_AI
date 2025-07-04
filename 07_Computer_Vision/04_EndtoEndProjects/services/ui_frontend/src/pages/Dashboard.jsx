import React from "react";

const Dashboard = () => {
  return (
    <div className="p-8 bg-gray-100 dark:bg-gray-800 rounded-lg shadow">
      <h2 className="text-xl font-bold text-gray-900 dark:text-white">
        Welcome to the Dashboard
      </h2>
      <p className="mt-2 text-gray-700 dark:text-gray-300">
        This changes based on the theme.
      </p>
    </div>
  );
};

export default Dashboard;

