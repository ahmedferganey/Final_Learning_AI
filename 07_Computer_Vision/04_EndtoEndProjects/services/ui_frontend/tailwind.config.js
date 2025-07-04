/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx,ts,tsx}", // This line ensures Tailwind scans your files
  ],
  darkMode: "class", // <- required for toggle to work
  theme: {
    extend: {},
  },
  plugins: [],
};

