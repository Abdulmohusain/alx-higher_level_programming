#!/usr/bin/node
const list = require('./100-data').list;
const newList = list.map((element, index) => element * (index + 1));
console.log(list);
console.log(newList);
