/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,js}",
    "./templates/**/*.html", // Templates at the project level
    "./**/templates/**/*.html", // Template  inside apps
  ],
  theme: {
    extend: {
      colors: {
        primary: "#E5004F", // Bold Red
        secondary: "#FFEEF5", // Soft Pink
        accent: "#1A1A1A", // Dark Gray/Black
        hover: "#C40042", // Deep Red (For Warnings)
        error: "#FF1744", // Darker Red for Hover
      },
    },
  },
  plugins: [],
};
