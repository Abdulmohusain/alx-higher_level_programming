#!/usr/bin/node
const Rectangle = require('./5-square');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        if (c === undefined) {
          process.stdout.write('X');
        } else {
          process.stdout.write(c);
        }
      }
      process.stdout.write('\n');
    }
  }
};
