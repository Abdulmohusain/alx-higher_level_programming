#!/usr/bin/node
const argv = process.argv;
if (argv[2] === undefined) {
  console.log('Missing size');
} else {
  const num = parseInt(argv[2]);
  if (isNaN(num)) {
    console.log('Missing size');
  } else {
    for (let i = 0; i < num; i++) {
      for (let j = 0; j < num; j++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }
}
