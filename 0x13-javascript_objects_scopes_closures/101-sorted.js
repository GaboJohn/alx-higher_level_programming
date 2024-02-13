#!/usr/bin/node
const dict = require('./101-data').dict;

const total = Object.entries(dict);
const len = Object.values(dict);
const num = [...new Set(len)];
const newDict = {};
for (const n in num) {
  const x = [];
  for (const y in total) {
    if (total[y][1] === num[n]) {
      x.unshift(total[y][0]);
    }
  }
  newDict[num[n]] = x;
}
console.log(newDict);
