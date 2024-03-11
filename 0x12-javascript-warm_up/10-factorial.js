#!/usr/bin/node
function factorial (num) {
  if (isNaN(num) || num === 1) {
    return (1);
  }
  return num * factorial(num - 1);
}
const argv = process.argv;
console.log(factorial(parseInt(argv[2])));
