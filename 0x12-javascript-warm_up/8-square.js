#!/usr/bin/node
// Loop
const Arguments = process.argv;
const i = parseInt(Arguments['2']);
if (Number.isNaN(i)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < i; x++) {
    console.log('X'.repeat(i));
  }
}
