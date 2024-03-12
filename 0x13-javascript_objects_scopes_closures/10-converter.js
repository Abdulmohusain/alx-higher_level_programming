#!/usr/bin/node
exports.converter = function (base) {
  return function (num) {
    return (base * (Math.floor(num / base)) + (num % base));
  };
};
