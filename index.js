const FtpSrv = require('ftp-srv');
const fs = require('fs');
const path = require('path');

// Define the path to the 'files' folder
const filesFolderPath = path.join(__dirname, 'files');

// Create the 'files' folder if it doesn't exist
if (!fs.existsSync(filesFolderPath)) {
  fs.mkdirSync(filesFolderPath);
  console.log(`Created 'files' folder at: ${filesFolderPath}`);
} else {
  console.log(`'files' folder already exists at: ${filesFolderPath}`);
}

// Define the FTP server
const ftpServer = new FtpSrv({
  url: "ftp://0.0.0.0:21", // Listen on all interfaces, port 21
  anonymous: true, // Allow anonymous login
  greeting: ["Welcome to My FTP Server"], // Custom greeting message
});

// Handle client connections
ftpServer.on('login', ({ connection, username, password }, resolve, reject) => {
  console.log(`User ${username} connected`);

  // Allow all users (for demonstration purposes)
  if (username === 'anonymous' && password === '') {
    return resolve({ root: filesFolderPath }); // Set the root directory for the user
  } else {
    return reject(new Error('Invalid username or password'));
  }
});

// Handle server errors
ftpServer.on('client-error', ({ connection, context, error }) => {
  console.error(`Client error: ${error.message}`);
});

// Start the FTP server
ftpServer.listen()
  .then(() => {
    console.log('FTP server is running on ftp://0.0.0.0:21');
  })
  .catch((err) => {
    console.error('Failed to start FTP server:', err);
  });
