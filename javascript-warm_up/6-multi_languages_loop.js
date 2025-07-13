#!/usr/bin/node
const lines = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let out = '';

for (const line of lines) {
  out += `${line}\n`;
}

console.log(out.trim());
