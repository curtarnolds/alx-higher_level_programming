#!/usr/bin/node

const request = require('request').get;

const url = process.argv[2];
request(url, (error, response) => {
  if (!error) {
    console.log(response.statusCode);
  }
});
