module.exports = {
  plugins: {
    autoprefixer: {
      // https://github.com/browserslist/browserslist#queries
      browsers: [
        '> 0.5%',
        'last 2 versions',
        'Firefox ESR',
        'not dead',
      ],
    },
  },
};
