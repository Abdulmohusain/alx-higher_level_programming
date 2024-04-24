#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const args = process.argv;
const path = args[3];
const options = {
  url: args[2],
  method: 'GET'
};

request(options, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(path, body, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
