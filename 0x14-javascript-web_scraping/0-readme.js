#!/usr/bin/node
const file = require('fs');
file.readFile(process.argv[2], 'utf8', (e, data) => {
  console.log(e || data);
});
