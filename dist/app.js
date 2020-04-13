"use strict";

var express = require('express');

var app = express();
var port = 3000;
app.get('/', function (req, res) {
  res.send('Hello from Express');
});
app.listen(port, function () {
  return console.log("Express is listening on ".concat(port));
});