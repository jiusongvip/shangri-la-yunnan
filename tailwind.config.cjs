/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Outfit", "ui-sans-serif", "system-ui", "sans-serif"],
        display: ["Outfit", "ui-sans-serif", "system-ui", "sans-serif"],
      },
      colors: {
        accent: "#15803d",
        "accent-light": "#22c55e",
        surface: "#f8f9fb",
        "surface-alt": "#f1f5f9",
        ink: "#0f172a",
        "ink-muted": "#475569",
      },
    },
  },
  plugins: [],
};
