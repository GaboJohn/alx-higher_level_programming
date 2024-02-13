#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let n = 0; n < this.height; n++) {
      let w = '';
      for (let y = 0; y < this.width; y++) {
        w += c;
      }
      console.log(w);
    }
  }
}

module.exports = Square;
