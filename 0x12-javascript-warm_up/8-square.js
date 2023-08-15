#!/usr/bin/node

const argument = process.argv;
if (!isNaN(Number(argument[2]))) {
  let sampleString = '';
  for (let index = 0; index < Number(argument[2]); index++) {
    sampleString = sampleString + 'X';
  }
  let i = 0;
  while (i < Number(argument[2])) {
    console.log(sampleString);
    i++;
  }
} else {
  console.log('Missing size');
}
