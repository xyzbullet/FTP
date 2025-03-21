from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

# Define the root directory for the FTP server
FTP_ROOT = os.path.join(os.getcwd(), "files")

# Create the 'files' directory if it doesn't exist
if not os.path.exists(FTP_ROOT):
    os.makedirs(FTP_ROOT)
    logging.info(f"Created FTP root directory at: {FTP_ROOT}")
else:
    logging.info(f"FTP root directory already exists at: {FTP_ROOT}")

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

# Enable detailed logging for the FTP handler
handler.log_prefix = "[%(username)s@%(remote_ip)s] "

# Set up the server
address = ("0.0.0.0", 21)  # Listen on all interfaces, port 21
server = FTPServer(address, handler)

# Start the server
logging.info("FTP server is running on ftp://0.0.0.0:21")
logging.info("Press Ctrl+C to stop the server.")
try:
    server.serve_forever()
except KeyboardInterrupt:
    logging.info("FTP server stopped.")
except Exception as e:
    logging.error(f"An error occurred: {e}")
finally:
    server.close_all()
