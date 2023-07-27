/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html"],
  theme: {
    extend: {
      colors: {
        'red': '#703030',
        'grey': '#2F343B',
        'green': '#7E827A',
        'teak': '#E3CDA4',
        'maroon': '#C77966',
      }
    },
  },
  plugins: [
    require('@tailwindcss/aspect-ratio'),
  ],
}

