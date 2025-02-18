// tailwind.config.js
const theme = require('./src/styles/theme');

module.exports = {
  content: [
    './src/**/*.{js,jsx,ts,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        primary: theme.colors.primary,
        background: theme.colors.background,
        text: theme.colors.text,
        border: theme.colors.border,
      },
      spacing: {
        layout: theme.spacing.layout,
        section: theme.spacing.section,
        element: theme.spacing.element,
      },
    },
  },
  plugins: [],
};