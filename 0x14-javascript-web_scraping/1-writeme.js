#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
const text = process.argv[3];
fs.write(file, 'utf-8', text, (err) =>{
    if (err){
        console.log(err);
    }
});