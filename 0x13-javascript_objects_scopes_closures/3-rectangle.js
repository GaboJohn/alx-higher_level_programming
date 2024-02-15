#!/usr/bin/node

class Rectangle {
  constructor (width, height) {
    if ((width > 0) && (height > 0)) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    for (let n = 0; n < this.height; n++) {
      let w = '';
      for (let y = 0; y < this.width; y++) {
        w += 'X';
      }
      console.log(w);
    }
  }
}

module.exports = Rectangle;
