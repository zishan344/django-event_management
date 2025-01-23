/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,js}",
    "./templates/**/*.html", // Templates at the project level
    "./**/templates/**/*.html", // Template  inside apps
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
