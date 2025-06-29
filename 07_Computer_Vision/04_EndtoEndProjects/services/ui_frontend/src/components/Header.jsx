import React from "react";
import { motion } from "framer-motion";
import { textSlideDown } from "../utils/animations";


const Header = () => {
  return (
    <header className="bg-blue-600 text-white py-4 px-6 shadow">
      <motion.h1 {...textSlideDown} className="text-2xl font-semibold">
        Computer Vision App
      </motion.h1>
    </header>
  );
};

export default Header;

