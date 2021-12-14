#!/usr/bin/node

let contador = 0;
exports.logMe = function (item) {
  console.log(contador + ': ' + item);
  contador++;
};
