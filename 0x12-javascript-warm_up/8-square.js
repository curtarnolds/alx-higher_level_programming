#!/usr/bin/node

const argument = process.argv;
if (!isNaN(Number(argument[2]))) {
  const array = [];
  let i = 0;
  while (i < argument[2]) {
    array.push('X');
    i++;
  }
  i = 0;
  while (i < argument[2]) {
    console.log(...array);
    i++;
  }
} else {
  console.log('Missing size');
}
