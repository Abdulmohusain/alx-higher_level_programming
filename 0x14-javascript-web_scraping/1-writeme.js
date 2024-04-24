#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
const path = args[2];
const string = args[3];
fs.writeFile(path, string, 'utf8', (error) => {
  if (error) {
    console.log(error);
  }
});
