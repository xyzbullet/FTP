from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os

# Define the root directory for the FTP server
FTP_ROOT = os.path.join(os.getcwd(), "files")

# Create the 'files' directory if it doesn't exist
if not os.path.exists(FTP_ROOT):
    os.makedirs(FTP_ROOT)
    print(f"Created FTP root directory at: {FTP_ROOT}")
else:
    print(f"FTP root directory already exists at: {FTP_ROOT}")

# Set up an authorizer to manage users
authorizer = DummyAuthorizer()

# Add anonymous user (no password required)
authorizer.add_anonymous(FTP_ROOT)

# Optionally, add authenticated users
# authorizer.add_user("username", "password", FTP_ROOT, perm="elradfmw")

# Set up the FTP handler
handler = FTPHandler
handler.authorizer = authorizer

# Customize the banner (optional)
handler.banner = "Welcome to My Python FTP Server"

# Set up the server
address = ("0.0.0.0", 21)  # Listen on all interfaces, port 21
server = FTPServer(address, handler)

# Start the server
print("FTP server is running on ftp://0.0.0.0:21")
print("Press Ctrl+C to stop the server.")
server.serve_forever()
