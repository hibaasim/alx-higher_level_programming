#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let sqr = '';
      for (let j = 0; j < this.width; j++) {
        sqr += c;
      }
      console.log(sqr);
    }
  }
}

module.exports = Square;
