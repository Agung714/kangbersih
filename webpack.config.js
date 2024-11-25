const path = require('path');

module.exports = {
  entry: './static/src/input.js',
  output: {
    filename: 'output.js',
    path: path.resolve(__dirname, 'static/dist'),
  },
  mode: 'production',
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env'],
          },
        },
      },
    ],
  },
};
