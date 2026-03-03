
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        skyblue: "#3ABEFF",
        aviation: "#0B1D39",
        accent: "#FBBF24",
        soft: "#F8FAFC",
      },
      fontFamily: {
        sans: ["Inter", "ui-sans-serif"],
      },
    },
  },
  plugins: [
    require("@tailwindcss/forms"),
    require("@tailwindcss/typography"),
  ],
};