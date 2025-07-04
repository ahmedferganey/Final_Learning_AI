import React from "react";

const Footer = () => {
  return (
    <footer className="bg-gray-100 dark:bg-gray-800 text-gray-700 dark:text-gray-300 py-4 px-6 mt-auto shadow-inner">
      <div className="max-w-7xl mx-auto flex flex-col sm:flex-row justify-between items-center gap-2 text-sm text-center sm:text-left">
        <p>&copy; 2025 <span className="font-semibold">Faragello Inc.</span> All rights reserved.</p>
        <p className="text-xs text-gray-500 dark:text-gray-400">Made with 💻 by Ahmed Ferganey</p>
      </div>
    </footer>
  );
};

export default Footer;

