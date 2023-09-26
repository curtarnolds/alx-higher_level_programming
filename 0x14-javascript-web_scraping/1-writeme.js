#!/usr/bin/node

const fs = require('fs').promises;

async function writeFile (filePath, str) {
  try {
    await fs.writeFile(filePath, str, 'utf-8');
  } catch (error) {
    console.error(error);
  }
}

writeFile(process.argv[2], process.argv[3]);
