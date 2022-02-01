#!/usr/bin/node
const request = require('request');
const editor = require('fs')
const file = process.argv[3];
const url = process.argv[2];
request(url, function (err, response, body) {
	if (err) {
		console.log(err);
}
	else if (response.statusCode === 200) {
	
	editor.writefile(file, body, 'utf-8');
}
	else {
	console.log(err);
}
});
