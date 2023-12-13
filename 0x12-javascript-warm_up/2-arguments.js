#!/usr/bin/node
const argv = process.argv;
if (Object.keys(argv).length === 3) {
  console.log('Argument found');
} else if (Object.keys(argv).length < 3) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
