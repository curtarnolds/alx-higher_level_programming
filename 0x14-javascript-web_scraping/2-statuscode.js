#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const response = request(url, (error, response, body) => console.log(`code: ${response && response.statusCode}`));
