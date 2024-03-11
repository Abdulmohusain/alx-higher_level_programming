#!/usr/bin/node
const argv = process.argv;
let highest = 0;
let secondHighest = 0;
if (argv.length < 4) {
  console.log(secondHighest);
} else {
  for (let i = 2; i < argv.length; i++) {
    const num = parseInt(argv[i]);
    if (num > highest) {
      secondHighest = highest;
      highest = num;
    } else if (num < highest) {
      if (num > secondHighest) {
        secondHighest = num;
      }
    }
  }
  console.log(secondHighest);
}
