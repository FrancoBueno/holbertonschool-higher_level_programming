#!/usr/bin/node
// Loop
const Arguments = process.argv;
function add (a, b) {
  return parseInt(a) + parseInt(b);
}
console.log(add(Arguments['2'], Arguments['3']));
