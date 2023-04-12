#!/usr/bin/node
const length = process.argv.length;
if (length <= 3) {
  console.log(0);
} else {
  const argsNum = process.argv.map(Math.floor)
    .slice(2, length)
    .sort((first, last) => first - last);

  console.log(argsNum[argsNum.length - 2]);
}
