#!/usr/bin/node

const request = require('request').get;

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(url, (error, response, body) => {
  if (!error && response) {
    console.log(`${JSON.parse(body).title}`);
  }
});
