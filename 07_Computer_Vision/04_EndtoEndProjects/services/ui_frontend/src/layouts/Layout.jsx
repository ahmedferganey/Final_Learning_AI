import React from "react";
import Header from "./Header";
import Footer from "./Footer";
import Sidebar from "./Sidebar";
import { Outlet } from "react-router-dom";

const Layout = () => (
  <div className="flex flex-col min-h-screen">
    <Header />
    <div className="flex flex-1">
      <Sidebar />
      <main className="flex-1 p-8 bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-white">
        <Outlet /> {/* Renders Home, Dashboard, etc. */}
      </main>
    </div>
    <Footer />
  </div>
);

export default Layout;

