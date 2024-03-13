#!/usr/bin/node
const myList = require('./100-data.js').list;
const newList = myList.map((element, index) => element * index);
console.log(myList);
console.log(newList);
