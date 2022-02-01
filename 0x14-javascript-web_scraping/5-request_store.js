#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const file = process.argv[3];
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(file, body, 'utf-8', function (err) {
      if (err) console.error(err);
    });
  }
});
