#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let contador = 0;

  for (const x in list) {
    if (list[x] === searchElement) {
      contador++;
    } else { continue; }
  }
  return contador;
};
