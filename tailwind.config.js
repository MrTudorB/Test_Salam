module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'sidebar': '#1a1a1a',
        'main-bg': '#000000',
        'accent-orange': '#ff6b4a',
      },
      backgroundImage: {
        'gradient-anchor': 'linear-gradient(180deg, #1a3045 0%, #0d1720 100%)',
        'gradient-wildcard': 'linear-gradient(180deg, #3a1f1f 0%, #1a0f0f 100%)',
        'gradient-zenith': 'linear-gradient(180deg, #1f3a1f 0%, #0f1a0f 100%)',
      },
    },
  },
  plugins: [],
} 