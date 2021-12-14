#!/usr/bin/node
let lista = require('./100-data').list;

const arrai2 = lista.map((x, index) => x * index);

console.log(lista);
console.log(arrai2);

