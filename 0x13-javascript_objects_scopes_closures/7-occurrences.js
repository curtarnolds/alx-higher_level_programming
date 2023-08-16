#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const key in list) {
    if (list[key] === searchElement) {
      count++;
    }
  }
  return count;
};
