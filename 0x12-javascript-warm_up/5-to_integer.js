#!/usr/bin/node
const argv = process.argv;
if (argv[2] === undefined) {
  console.log('Not a number');
} else {
  const num = parseInt(argv[2]);
  if (isNaN(argv[2])) {
    console.log('Not a number');
  } else {
    console.log(num);
  }
}
