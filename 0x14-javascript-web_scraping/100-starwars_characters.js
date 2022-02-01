#!/usr/bin/node

const request = require('request');
const num = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films';
request(url, function (err, response, body) {
  if (!err) {
    const results = JSON.parse(body).results;
    for (let x = 0; results[x]; x++) {
      if (x + 1 === parseInt(num)) {
        const chars = results[x].characters;
        for (let i = 0; chars[i]; i++) {
          request(chars[i], function (error, response, body) {
            if (!err) {
              console.log(JSON.parse(body).name);
            }
          });
        }
      }
    }
  }
	else {
		console.log(err)
}
});
