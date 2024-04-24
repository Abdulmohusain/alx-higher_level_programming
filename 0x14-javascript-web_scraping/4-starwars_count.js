#!/usr/bin/node
const request = require('request');
const args = process.argv;
const options = {
  url: args[2],
  method: 'GET',
  json: true
};
let count = 0;

request(options, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = body.results;

    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        const regex = /\/18\//;
        if (regex.test(characters[j])) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
