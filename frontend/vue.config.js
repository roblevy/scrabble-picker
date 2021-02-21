const path = require("path");

module.exports = {
  publicPath: process.env.VUE_APP_STATIC_URL,
  outputDir: path.resolve(__dirname, "../static", "scrabble_picker"),
  indexPath: path.resolve(__dirname, "../templates/", "scrabble_picker", "index.html"),
};

