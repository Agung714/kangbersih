module.exports = {
  content: [
    "./templates/**/*.html", 
    "node_modules/preline/dist/*.js"
  ],
  theme: {
    extend: {
      screens: {
        'xs': '360px',
        'sm': '640px',
        'md': '768px',
        'lg': '1024px',
        'xl': '1280px',
        '2xl': '1536px',
      },
      colors: {
        'custom-blue': '#5A72A0',
      },
    },
  },
  plugins: [
    require('preline/plugin'),
  ],
  darkMode: 'false',
};
