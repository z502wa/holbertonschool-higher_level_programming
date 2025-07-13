#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

/* update value without var */
myObject.value = 89;

console.log(myObject);
