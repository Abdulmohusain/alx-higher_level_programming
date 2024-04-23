#!/usr/bin/node
const request = require('request');
const args = process.argv;
const options = {
  url: 'https://swapi-api.alx-tools.com/api/films/' + args[2],
  method: 'GET',
  json: true
};
request(options, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  console.log(body.title);
});
