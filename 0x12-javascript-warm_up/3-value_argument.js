#!/usr/bin/node
// args in Javascript
const Arguments = process.argv;
const lengthArg = process.argv.length;
if (lengthArg < 3) {
  console.log('No argument');
}
if (Arguments['2']) {
  console.log(Arguments['2']);
}
