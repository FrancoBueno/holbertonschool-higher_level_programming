#!/usr/bin/node
const request = require('request');
const movieid = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url + movieid, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const json = JSON.parse(body);
    console.log(json.title);
  } else {
    console.log(err);
  }
});
