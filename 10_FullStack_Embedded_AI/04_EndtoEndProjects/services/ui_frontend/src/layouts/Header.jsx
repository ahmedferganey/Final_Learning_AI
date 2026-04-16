import React, { useState } from "react";
import { motion } from "framer-motion";
import { textSlideDown } from "../utils/animations";

import AboutLink from "../components/common/AboutLink/AboutLink";
import UserLogin from "../components/auth/UserLogin/index";
import DarkModeToggle from "../components/common/DarkModeToggle/DarkModeToggle";

const Header = () => {
  const [toastMessage, setToastMessage] = useState(null);

  const handleThemeToggle = (isDark) => {
    setToastMessage(isDark ? "Dark mode enabled" : "Light mode enabled");
    setTimeout(() => setToastMessage(null), 1000);
  };

  return (
    <header className="bg-slate-800 text-white px-4 py-3 shadow rounded-xl">
      <div className="flex flex-col sm:flex-row sm:justify-between sm:items-center gap-4">
        {/* Logo with animation */}
        <motion.h1
          className="text-2xl sm:text-3xl font-extrabold tracking-tight text-yellow-400 drop-shadow-sm"
          initial={textSlideDown.initial}
          animate={textSlideDown.animate}
          transition={textSlideDown.transition}
        >
          🍕 Pizza Store
        </motion.h1>

        {/* Right-side controls */}
        <div className="flex flex-wrap justify-start sm:justify-end items-center gap-3">
          <AboutLink />
          <UserLogin />
          <DarkModeToggle onToggle={handleThemeToggle} />
        </div>
      </div>

      {/* Toast Notification */}
      {toastMessage && (
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: 20 }}
          className="fixed bottom-6 right-6 bg-gray-900 text-white px-4 py-2 rounded shadow-lg z-50"
        >
          {toastMessage}
        </motion.div>
      )}
    </header>
  );
};

export default Header;

