#!/usr/bin/node

const request = require('request').get;

const url = `${process.argv[2]}`;
request(url, (error, response, body) => {
  if (!error && response) {
    const numOfMovies = JSON.parse(body).results.map(result => result.characters.filter(char => char.includes('18'))).filter(res => res.length !== 0).length;
    console.log(numOfMovies);
  }
});
