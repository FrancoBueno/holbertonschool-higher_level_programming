#!/usr/bin/node

let maximo = 0;
const Arguments = process.argv.slice(2);
if (Arguments.length > 1) {
  Arguments.sort();
  maximo = Arguments[Arguments.length - 2];
}
console.log(maximo);
