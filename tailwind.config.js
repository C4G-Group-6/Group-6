/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './templates/**/*.html',
    './apps/**/*.html',
<<<<<<< HEAD
    './apps/**/*.py',
=======
>>>>>>> ff21b459de8db17bb1bb0512dad38e2e6cb193ca
    './static/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        'nav-bg': '#1F452D',
        'button-bg': '#ADD6C5',
      },
      fontFamily: {
        'heading': ['Inter', '-apple-system', 'Roboto', 'Helvetica', 'sans-serif'],
        'subtitle': ['Oswald', '-apple-system', 'Roboto', 'Helvetica', 'sans-serif'],
      },
    },
  },
  plugins: [require('daisyui')],
  daisyui: {
    themes: ['light'],
  },
}
