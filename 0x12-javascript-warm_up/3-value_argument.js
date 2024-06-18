#!/usr/bin/node
// prints the first argument passed to it:
// If no arguments are passed to the script, print “No argument”

const arg = process.argv[2];
if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
