#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const id = 18;

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const i in films) {
      const filmint = films[i].characters;
      for (const x in filmint) {
        if (filmint[x].includes(id)) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log(err);
  }
});
