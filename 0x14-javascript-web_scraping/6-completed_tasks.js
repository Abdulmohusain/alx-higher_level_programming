#!/usr/bin/node
const request = require('request');
const args = process.argv;
const options = {
  url: args[2],
  method: 'GET',
  json: true
};

request(options, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const result = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0
  };
  const users = body;
  for (const user of users) {
    if (user.completed) {
      switch (user.userId) {
        case 1:
          result['1']++;
          break;
        case 2:
          result['2']++;
          break;
        case 3:
          result['3']++;
          break;
        case 4:
          result['4']++;
          break;
        case 5:
          result['5']++;
          break;
        case 6:
          result['6']++;
          break;
        case 7:
          result['7']++;
          break;
        case 8:
          result['8']++;
          break;
        case 9:
          result['9']++;
          break;
        case 10:
          result['10']++;
          break;
      }
    }
  }
  console.log(result);
});
