#!/usr/bin/node

exports.esrever = function (list) {
  const tempList = [];
  let i = 0;
  const listLength = list.length;
  while (i < listLength) {
    tempList[i] = list[listLength - 1 - i];
    i++;
  }
  return tempList;
};
