import yaml
from ftplib import FTP
import json


# Load config (assuming config is loaded as a dictionary from JSON or similar)
with open("config.yml", "r") as file:
    config = yaml.safe_load(file)

ftp = FTP(config["ftp_host"])  # Use plain FTP, not FTP_TLS
ftp.login(config["ftp_user"], config["ftp_pwd"])

# Optional: navigate to directory
# ftp.cwd('/some/path')

# Example operation: list files
ftp.retrlines('LIST')
# Upload index.html
filename = 'index.html'
with open("myproject/templates/index.html", "rb") as file:
    ftp.storbinary(f"STOR {filename}", file)

print(f"{filename} uploaded successfully.")
# Always close the connection when done
ftp.quit()
