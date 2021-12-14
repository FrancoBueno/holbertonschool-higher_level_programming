#!/usr/bin/node
exports.converter = function (base) {
  function convertidor (c) {
    return c.toString(base);
  }
  return convertidor;
};
