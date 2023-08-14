#!/usr/bin/node

const argument = process.argv;
typeof argument[2] !== 'undefined' ? console.log(argument[2]) : console.log('No Argument');
