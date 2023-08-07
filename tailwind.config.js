/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html"],
  theme: {
    extend: {
      colors: {
        'red': '#41ead4',
        'grey': '#2F343B',
        'green': '#74a4bc',
        'teak': '#BAA885',
        'maroon': '#ac9fbb',
        'purp': '#7d83ff',
        'blue': '#d4dcff'
      }
    },
  },
  plugins: [
    require('@tailwindcss/aspect-ratio'),
  ],
}

