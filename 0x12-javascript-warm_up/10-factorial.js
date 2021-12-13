#!/usr/bin/node
// Factorial
const Arguments = process.argv;
const Alfredo = parseInt(Arguments['2']);
function factorial (Alfredo) {
  if (Alfredo === 0) {
    return 1;
  }
  return Alfredo * factorial(Alfredo - 1);
}
console.log(factorial(Alfredo));
