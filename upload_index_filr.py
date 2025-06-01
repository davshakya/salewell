import yaml
from ftplib import FTP
import os

def load_config(path="config.yml"):
    """Load configuration from a YAML file."""
    try:
        with open(path, "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        raise Exception(f"Configuration file '{path}' not found.")
    except yaml.YAMLError as e:
        raise Exception(f"Error parsing YAML file: {e}")

def upload_file(ftp, local_path, remote_filename):
    """Upload a file to the FTP server."""
    if not os.path.exists(local_path):
        raise FileNotFoundError(f"Local file '{local_path}' does not exist.")

    with open(local_path, "rb") as file:
        ftp.storbinary(f"STOR {remote_filename}", file)
    print(f"'{remote_filename}' uploaded successfully.")

def list_directory(ftp):
    """List files and directories in the current FTP path."""
    print("Directory listing:")
    try:
        items = []
        ftp.retrlines('LIST', items.append)
        for item in items:
            print(item)
    except Exception as e:
        print(f"Failed to list directory: {e}")


def main():
    config = load_config()

    try:
        ftp = FTP(config["ftp_host"])
        ftp.set_debuglevel(0)  # Set to 2 for full FTP debug
        ftp.login(config["ftp_user"], config["ftp_pwd"])
        ftp.set_pasv(True)  # Enable passive mode
        print(f"Connected to FTP: {config['ftp_host']}")

        # Navigate to target directory if provided
        if "ftp_target_dir" in config:
            ftp.cwd('/')
            print("Changed to target directory:", ftp.pwd())
        else:
            print("Current directory:", ftp.pwd())

        # List directory
        list_directory(ftp)

        # Upload file
        local_file_path = "myproject/templates/index.html"
        remote_file_name = "index.html"
        upload_file(ftp, local_file_path, remote_file_name)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        try:
            ftp.quit()
            print("FTP connection closed.")
        except:
            pass


if __name__ == "__main__":
    main()

