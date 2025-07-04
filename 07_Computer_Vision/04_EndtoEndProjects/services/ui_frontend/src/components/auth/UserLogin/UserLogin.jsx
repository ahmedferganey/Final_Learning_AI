// src/components/auth/UserLogin/UserLogin.jsx
import React, { useState } from "react";
import { motion } from "framer-motion";
import { textSlideDown } from "../../../utils/animations";
import LoginModal from "../LoginModal/LoginModal";
import SignupModal from "../SignupModal/SignupModal";
import useAuth from "../../../hooks/useAuth";

const UserLogin = () => {
  const [isLoginOpen, setIsLoginOpen] = useState(false);
  const [isSignupOpen, setIsSignupOpen] = useState(false);
  const { user, logout } = useAuth();

  const handleClick = () => {
    if (user) {
      logout();
    } else {
      setIsLoginOpen(true);
    }
  };

  const handleSwitchToSignup = () => {
    setIsLoginOpen(false);
    setIsSignupOpen(true);
  };

  const handleSwitchToLogin = () => {
    setIsSignupOpen(false);
    setIsLoginOpen(true);
  };

  return (
    <>
      <motion.div
        className="text-sm text-white hover:underline cursor-pointer"
        initial={textSlideDown.initial}
        animate={textSlideDown.animate}
        transition={textSlideDown.transition}
        onClick={handleClick}
      >
        {user ? "Logout" : "Login"}
      </motion.div>

      <LoginModal
        isOpen={isLoginOpen}
        onClose={() => setIsLoginOpen(false)}
        onSignupClick={handleSwitchToSignup} // ✅ Pass this to switch
      />

      <SignupModal
        isOpen={isSignupOpen}
        onClose={() => setIsSignupOpen(false)}
        onLoginClick={handleSwitchToLogin} // ✅ Optional: switch back
      />
    </>
  );
};

export default UserLogin;

