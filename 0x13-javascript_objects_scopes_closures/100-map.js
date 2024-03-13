#!/usr/bin/node
const myList = require('./100-data').list;
const newList = myList.map((element, index) => element * (index + 1));
console.log(myList);
console.log(newList);
