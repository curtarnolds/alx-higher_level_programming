#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    let xRect = '';
    for (let j = 0; j < this.height; j++) {
      xRect = xRect + c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(xRect);
    }
  }
};