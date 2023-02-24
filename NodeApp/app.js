const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  const spawn = require("child_process").spawn;
  const pythonProcess = spawn('python',["/workspaces/IBM_Project/trial.py", "http://www.somethingsomething.com/video.mkv"]);

  pythonProcess.stdout.on('data', (data) => {
    console.log("Runninggg");
    res.send(data.toString());
    res.end("Hellooooooooo");
   });
  res.end('Hello World');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});