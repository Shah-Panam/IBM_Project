const express = require('express')
const { spawn } = require('child_process');
var cors = require('cors')
const app = express()
const port = 3000

app.use(cors())

app.get('/trial/:path', (req, res) => {

  var dataToSend;
  var dataError;
  // spawn new child process to call the python script
  const python = spawn('python', ["/workspaces/IBM_Project/trial.py", "http://www.somethingsomething.com/video.mkv"]);
  // collect data from script
  python.stdout.on('data', function (data) {
    console.log('Pipe data from python script ...');
    dataToSend = data.toString();
  });
  python.stderr.on('data', function (data) {
    console.log('Pipe data from python script ...');
    dataError = data.toString();
  });
  // in close event we are sure that stream from child process is closed
  python.on('close', (code) => {
    console.log(`child process close all stdio with code ${code}`);
    // send data to browser
    console.log(dataToSend);
    console.log(dataError);
    res.send(dataToSend)
  });

})

app.get('/myapi', function (req, res) {

  // const newf = "someval";
  // try {
    const newf = req.query.newf;
  // }
  // catch {
  //   console.log("Error newf not found");
  // }

  var dataToSend;
  var dataError;
  // spawn new child process to call the python script
  const python = spawn('python', ["/workspaces/IBM_Project/trial.py", newf]);
  // collect data from script
  python.stdout.on('data', function (data) {
    console.log('Pipe data from python script ...');
    dataToSend = data.toString();
  });
  python.stderr.on('data', function (data) {
    console.log('Pipe data from python script ...');
    dataError = data.toString();
  });
  // in close event we are sure that stream from child process is closed
  python.on('close', (code) => {
    console.log(`child process close all stdio with code ${code}`);
    // send data to browser
    console.log(dataToSend);
    console.log(dataError);
    res.send(dataToSend)
  });

})

var server = app.listen(8080, function() {
 console.log("Listening on 8080");
})

app.listen(port, () => console.log(`Example app listening on port 
${port}!`))