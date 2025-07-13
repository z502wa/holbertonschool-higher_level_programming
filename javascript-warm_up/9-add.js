#!/usr/bin/node
const add = (a, b) => a + b;

const a = Number(process.argv[2]);
const b = Number(process.argv[3]);

console.log(add(a, b));
