#!/usr/bin/node
const squareClass = require('./5-square');

module.exports = class Square extends squareClass {
  charPrint (c = 'X') {
    if (this.height > 0) {
      let xRect = '';
      for (let j = 0; j < this.height; j++) {
        xRect = xRect + c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(xRect);
      }
    }
  }
};
