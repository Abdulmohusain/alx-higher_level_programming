#!/usr/bin/node
exports.converter = function (base) {
  return function (num) {
    if (base === 10) {
      return (base * (Math.floor(num / base)) + (num % base));
    } else {
      return (base * (Math.floor(num.toString(16) / base)) + (num.toString(16) % base));
    }
  };
};
