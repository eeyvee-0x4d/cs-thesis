module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    ],
  theme: {
    minHeight: {
      '1/8': '8vh'
    },
    extend: {
      keyframes: {
        'fade-in-left': {
          '0%': {
            opacity: '0',
            transform: 'translateY(10px)'
          },
          '100%': {
            opacity: '1',
            transform: 'translateY(0)'
          }
        }
      },
      animation: {
        'fade-in-left': 'fade-in-left 0.5s ease-out'
      }
    },
  },
  plugins: [],
}
