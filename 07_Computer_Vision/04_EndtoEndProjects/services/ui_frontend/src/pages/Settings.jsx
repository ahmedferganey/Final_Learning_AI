import React from "react";
import { Helmet } from "react-helmet-async";

const Settings = () => (
  <>
    <Helmet>
      <title>Settings | Pizza Store App</title>
      <meta name="description" content="Customize your app experience in settings." />
      <meta property="og:title" content="Settings | Pizza Store App" />
    </Helmet>

    <h1 className="text-2xl text-gray-800 dark:text-white">Settings</h1>
  </>
);

export default Settings;

