#!/usr/bin/node
// args in Javascript
const Arguments = process.argv;
if (Arguments['1']) {
  console.log('No argument');
}
if (Arguments['2']) {
  console.log(Arguments['2']);
}
