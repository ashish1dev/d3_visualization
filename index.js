const express = require('express')
const app = express()
const port = 3000
const path = require('path');

var inputFilePath = 'WCO_out_CC_Diabetes.csv';
const fs = require('fs');
const csv = require('csv-parser');

app.use(express.static('public'))

//
//   var words = [];
// fs.createReadStream(inputFilePath)
// .pipe(csv())
// .on('data', function(data){
//
//     try {
//         //perform the operation
//         // console.log("Input1 is: "+data.input_1+",Output is: "+data.Output);
//         words.push({'text':data.Word,'size' : data.Count});
//         print(words);
//         console.log(data);
//     }
//     catch(err) {
//         //error handler
//     }
// }).on('end',function(){
//     //some final operation
//   console.log(words);
//
//   'use strict';
//
// const fs = require('fs');
//
//
// let data = JSON.stringify(words);
// fs.writeFileSync('public/wco_cc_diabetes_data.js', data);
//
// });

// app.get('/', (req, res) => res.send(output))

app.get('/',function(req,res) {
  // res.sendFile('visualise.html');
   res.sendFile(path.join(__dirname+'/visualise.html'));
});

app.listen(port, () => console.log(`. app listening on port ${port}!`))
