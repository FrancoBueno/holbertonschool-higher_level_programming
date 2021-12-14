#!/usr/bin/node
exports.converter = function (base) {
  let ready = [];
  function convertidor (c) {
    ready = c.toString(base);
    return ready;
  }
  return convertidor;
};
