#!/usr/bin/node
const argument = process.argv;
function add (a, b) {
  const c = Number(a) + Number(b);
  console.log(c);
}

add(argument[2], argument[3]);
