// Import required modules
const express = require('express');
const multer  = require('multer');

// Create an instance of the express application
const app = express();

// Set up Multer to handle file uploads
const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, 'uploads/')
  },
  filename: function (req, file, cb) {
    cb(null, file.fieldname + '-' + Date.now())
  }
})

const upload = multer({ storage: storage })

// Set up a route to handle file uploads
app.post('/upload', upload.single('file'), function (req, res, next) {
  // File has been uploaded successfully
  res.send('File uploaded successfully');
})

// Serve the HTML file that includes the upload form
app.get('/', function(req, res) {
  res.sendFile(__dirname + '/index.html');
});

// Start the server
app.listen(3000, function() {
  console.log('Server started on port 3000');
});


// Set up a route to handle file uploads
app.post('/upload', upload.single('file'), function (req, res, next) {
  // File has been uploaded successfully
  res.send('File uploaded successfully');

  // Read the uploaded file
  const filePath = req.file.path;
  const fileType = req.file.mimetype;

  // If the file is an image, send it as a response
  if (fileType.startsWith('image/')) {
    res.sendFile(filePath);
  }
});

