#!/usr/bin/node
const argument = process.argv;
!isNaN(Number(argument[2])) ? console.log(`My number: ${argument[2]}`) : console.log('Not a number');
