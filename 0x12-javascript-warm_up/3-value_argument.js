#!/usr/bin/node
// args in Javascript
const Arguments = process.argv;
if (Arguments['2'] === undefined) {
  console.log('No argument');
}
if (Arguments['2']) {
  console.log(Arguments['2']);
}
