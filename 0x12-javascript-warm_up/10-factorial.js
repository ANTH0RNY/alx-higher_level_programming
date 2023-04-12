#!/usr/bin/node
function factorial (n) {
  if (!n) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const num = Math.floor(process.argv[2]);
console.log(factorial(num));
