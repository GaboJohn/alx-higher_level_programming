#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const len = Number(process.argv[2]);
  let num = 0;
  while (num < len) {
    console.log('X'.repeat(len));
    num++;
  }
}
