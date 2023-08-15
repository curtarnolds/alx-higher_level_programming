#!/usr/bin/node
const argument = process.argv;

function factorial (a) {
  if (isNaN(Number(a)) || Number(a) === 0) {
    return (1);
  }
  return Number(a) * factorial(Number(a) - 1);
}

console.log(factorial(argument[2]));
