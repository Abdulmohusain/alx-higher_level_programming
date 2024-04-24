#!/usr/bin/node
const request = require('request');
const args = process.argv;
const options = {
  url: 'https://swapi-api.alx-tools.com/api/films/' + args[2],
  method: 'GET',
  json: true
};

function makeSyncRequest (url) {
  return new Promise((resolve, reject) => {
    const options = {
      url,
      method: 'GET',
      json: true
    };
    request(options, function (error, response, body) {
      if (error) {
        reject(error);
      } else {
        resolve(body.name);
      }
    });
  });
}

async function getData (url) {
  const data = await makeSyncRequest(url);
  console.log(data);
}

request(options, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const characters = body.characters;

  for (const character of characters) {
    getData(character);
  }
});
