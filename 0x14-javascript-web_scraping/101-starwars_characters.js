#!/usr/bin/node

const request = require('request').get;

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, (error, response, body) => {
  if (!error && response) {
    const characters = JSON.parse(body).characters;

    const getCharacterName = (characters, index = 0) => {
      if (index < characters.length) {
        const char = characters[index];
        request(char, (err, resp, data) => {
          if (!err && resp) {
            console.log(JSON.parse(data).name);
            getCharacterName(characters, index + 1);
          }
        });
      }
    };
    getCharacterName(characters);
  }
});
