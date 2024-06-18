#!/usr/bin/node
// prints x times “C is fun”
// Where x is the first argument of the script
// If the first argument can’t be converted to an integer, print “Missing number of occurrences”

const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
