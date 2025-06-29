import React from "react";
import Header from "./Header";
import Footer from "./Footer";
import Sidebar from "./Sidebar";

const Layout = ({ children }) => {
  return (
    <div className="flex flex-col min-h-screen">
      {/* Header */}
      <Header />

      {/* Sidebar + Main */}
      <div className="flex flex-1">
        <Sidebar />

        <main className="flex-1 p-8 bg-gray-50 overflow-auto">
          {children}
        </main>
      </div>

      {/* Optional Footer */}
      <Footer />
    </div>
  );
};

export default Layout;

