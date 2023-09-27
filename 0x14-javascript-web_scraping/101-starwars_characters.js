#!/usr/bin/node

const request = require('request').get;

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(url, (error, response, body) => {
  if (!error && response) {
    const characters = JSON.parse(body).characters;
    for (let i = 0; i < characters.length; i++) {
      const element = characters[i];
      request(element, (err, resp, data) => {
        if (!err && resp) {
          console.log(JSON.parse(data).name);
        }
      });
    }
    // characters.forEach(character => request(`${character}`, (err, resp, data) => {
    //   if (!err && resp) {
    //     console.log(JSON.parse(data).name);
    //   }
    // }));
  }
});
