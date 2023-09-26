#!/usr/bin/node

const fs = require('fs').promises;
const request = require('request').get;

const url = `${process.argv[2]}`;

async function writeFile (filePath, str) {
  try {
    await fs.writeFile(filePath, str, 'utf-8');
  } catch (error) {
    console.error(error);
  }
}

request(url, (error, response, body) => {
  if (!error && response) {
    writeFile(process.argv[3], body);
  }
});
