#!/usr/bin/node
const number = Math.floor(process.argv[2]);
if (number) {
  for (let i = 0; i < number; i++) {
    let row = '';
    for (let j = 0; j < number; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing Size');
}
