#!/usr/bin/node
//args in Javascript
const Arguments = process.argv.length;
if (Arguments == 3){
console.log('Argument found')
}
else if (Arguments < 3){
console.log('No argument')
}
else if (Arguments > 3){
console.log('Arguments found')
}
