// components/DarkModeToggle.jsx
import React, { useState, useEffect } from "react";
import { Moon, Sun } from "lucide-react";
import { AnimatePresence, motion } from "framer-motion";

const DarkModeToggle = ({ onToggle }) => {
  const [isDark, setIsDark] = useState(false);

  useEffect(() => {
    const systemQuery = window.matchMedia("(prefers-color-scheme: dark)");
    const stored = localStorage.getItem("theme");
    const initialDark = stored === "dark" || (!stored && systemQuery.matches);
    setIsDark(initialDark);
    document.documentElement.classList.toggle("dark", initialDark);
  }, []);

  const toggleTheme = () => {
    const newDark = !isDark;
    setIsDark(newDark);
    document.documentElement.classList.toggle("dark", newDark);
    localStorage.setItem("theme", newDark ? "dark" : "light");
    onToggle?.(newDark);
  };

  return (
    <button
      onClick={toggleTheme}
      className="bg-white dark:bg-gray-700 text-slate-800 dark:text-white px-3 py-2 rounded-full shadow hover:bg-slate-100 dark:hover:bg-gray-600 transition-colors duration-300 flex items-center justify-center"
      aria-label="Toggle Dark Mode"
      title="Toggle Dark Mode"
    >
      <AnimatePresence mode="wait">
        <motion.div
          key={isDark ? "sun" : "moon"}
          initial={{ rotate: 90, opacity: 0 }}
          animate={{ rotate: 0, opacity: 1 }}
          exit={{ rotate: -90, opacity: 0 }}
          transition={{ duration: 0.3 }}
        >
          {isDark ? <Sun size={20} /> : <Moon size={20} />}
        </motion.div>
      </AnimatePresence>
    </button>
  );
};

export default DarkModeToggle;
