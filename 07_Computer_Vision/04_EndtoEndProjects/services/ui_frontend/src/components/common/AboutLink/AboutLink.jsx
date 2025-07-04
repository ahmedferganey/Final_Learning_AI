// components/AboutLink.jsx
import React from "react";
import { Link } from "react-router-dom";
import { motion } from "framer-motion";
import { textSlideDown } from "../../../utils/animations";

const AboutLink = () => {
  return (
    <motion.div
      className="text-sm text-white hover:underline"
      initial={textSlideDown.initial}
      animate={textSlideDown.animate}
      transition={textSlideDown.transition}
    >
      <Link to="/about">About</Link>
    </motion.div>
  );
};

export default AboutLink;
