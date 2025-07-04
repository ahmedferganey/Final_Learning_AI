// src/components/LoginModal/index.jsx
import React, { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import useAuth from "../../../hooks/useAuth";

const LoginModal = ({ isOpen, onClose, onSignupClick }) => {
  const { login } = useAuth();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    setError("");

    const res = await login(username, password);
    if (!res.success) {
      setError(res.message);
    } else {
      onClose();
    }
  };

  return (
    <AnimatePresence>
      {isOpen && (
        <motion.div
          className="fixed inset-0 bg-black bg-opacity-60 backdrop-blur-sm flex items-center justify-center z-50"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
        >
          <motion.div
            className="bg-white dark:bg-gray-800 text-black dark:text-white p-6 rounded-xl shadow-lg w-80"
            initial={{ scale: 0.8, y: -50, opacity: 0 }}
            animate={{ scale: 1, y: 0, opacity: 1 }}
            exit={{ scale: 0.8, y: -50, opacity: 0 }}
            transition={{ duration: 0.3 }}
          >
            <h2 className="text-lg font-bold mb-4 text-center">Login</h2>
            <form onSubmit={handleLogin} className="flex flex-col space-y-3">
              <input
                type="text"
                placeholder="Email"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                className="p-2 rounded border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700"
                required
              />
              <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="p-2 rounded border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700"
                required
              />
              {error && <p className="text-red-500 text-sm">{error}</p>}
              <button
                type="submit"
                className="bg-blue-600 hover:bg-blue-700 text-white py-2 rounded"
              >
                Login
              </button>
              <button
                type="button"
                onClick={onClose}
                className="text-sm text-gray-500 hover:underline mt-2"
              >
                Cancel
              </button>
              <button
                type="button"
                onClick={() => {
                  onClose();
                  onSignupClick();
                }}
                className="text-sm text-blue-500 hover:underline mt-1"
              >
                Don’t have an account? Sign up
              </button>
            </form>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
};

export default LoginModal;

