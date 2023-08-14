#!/usr/bin/node

const argument = process.argv;
const array = [];
let i = 0;
while (i < Number(argument[2])) {
  array.push('X');
  i++;
}
i = 0;
while (i < Number(argument[2])) {
  console.log(...array);
  i++;
}
