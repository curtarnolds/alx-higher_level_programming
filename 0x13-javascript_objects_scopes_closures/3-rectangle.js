#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 || h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width > 0 && this.height > 0) {
      let xRect = '';
      for (let j = 0; j < this.width; j++) {
        xRect = xRect + 'X';
      }
      for (let i = 0; i < this.height; i++) {
        console.log(xRect);
      }
    }
  }
};
