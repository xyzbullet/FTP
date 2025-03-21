const FtpSrv = require('ftp-srv');

// Define the FTP server options
const ftpServer = new FtpSrv({
  url: "ftp://0.0.0.0:21", // Listen on all interfaces, port 21
  anonymous: true, // Allow anonymous login
  greeting: ["Welcome to My FTP Server"], // Custom greeting message
});

// Handle client connections
ftpServer.on('login', ({ connection, username, password }, resolve, reject) => {
  console.log(`User ${username} connected`);

  // Allow all users (for demonstration purposes)
  if (username === 'admin' && password === 'admin') {
    return resolve({ root: './files' }); // Set the root directory for the user
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
