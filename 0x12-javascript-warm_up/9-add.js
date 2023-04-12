#!/usr/bin/node
const number = Math.floor(process.argv[2]);
const num = Math.floor(process.argv[3]);
if (number && num) {
  console.log(number + num);
} else {
  console.log(`${'p' - 3}`);
}
