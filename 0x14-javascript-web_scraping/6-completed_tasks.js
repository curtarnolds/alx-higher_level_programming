#!/usr/bin/node

const request = require('request').get;

const url = `${process.argv[2]}`;
request(url, (error, response, body) => {
  if (!error && response) {
    const users = JSON.parse(body);
    const completedUsers = Object();
    users.forEach((member) => { if (typeof completedUsers[String(member.userId)] === 'number' && member.completed === true) { completedUsers[String(member.userId)] += 1; } else if (member.completed === true) { completedUsers[String(member.userId)] = 1; } });
    console.log(completedUsers);
  }
});
