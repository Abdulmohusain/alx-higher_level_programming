#!/usr/bin/node
const request = require('request');
const args = process.argv;
const options = {
  url: 'https://swapi-api.alx-tools.com/api/films/' + args[2],
  method: 'GET',
  json: true
};

function func2 (characterName) {
  console.log(characterName);
}

function func1 (characters) {
  for (const character of characters) {
    const options = {
      url: character,
      method: 'GET',
      json: true
    };
    request(options, function (error, response, body) {
      if (error) {
        console.log(error);
      }
      const characterName = body.name;
      func2(characterName);
    });
  }
}
request(options, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const characters = body.characters;
  func1(characters);
});
