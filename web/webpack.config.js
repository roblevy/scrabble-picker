module.exports = {
  mode: process.env.ENVIRONMENT || 'development',
  devtool: 'inline-source-map',
  devServer: {
    contentBase: './dist',
    proxy: {
      '/api': {
        target: `http://${process.env.API}:${process.env.API_PORT}`,
        pathRewrite: {'^/api' : ''}
      }
    }
  },
  module: {
    rules: [
      {
        test: /\.m?js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
        }
      }
    ],
  }
}
