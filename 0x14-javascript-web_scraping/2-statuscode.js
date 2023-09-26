#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const response = request(url, (response) => console.log(`code: ${response && response.statusCode}`));
