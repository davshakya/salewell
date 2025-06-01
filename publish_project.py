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
    """Upload a single file to the FTP server."""
    if not os.path.exists(local_path):
        raise FileNotFoundError(f"Local file '{local_path}' does not exist.")
    with open(local_path, "rb") as file:
        ftp.storbinary(f"STOR {remote_filename}", file)
    print(f"Uploaded file: {remote_filename}")

def upload_directory(ftp, local_dir, remote_dir):
    """Upload a directory (recursively) to the FTP server."""
    for root, dirs, files in os.walk(local_dir):
        # Relative path from the base local_dir
        rel_path = os.path.relpath(root, local_dir)
        if rel_path == ".":
            ftp_path = remote_dir
        else:
            ftp_path = os.path.join(remote_dir, rel_path).replace("\\", "/")

        # Create directory on FTP if it doesn't exist
        try:
            ftp.cwd(ftp_path)
        except:
            parts = ftp_path.strip("/").split("/")
            current_path = ""
            for part in parts:
                current_path += f"/{part}"
                try:
                    ftp.mkd(current_path)
                except:
                    pass  # Directory already exists or cannot be created
            ftp.cwd(ftp_path)

        # Upload files in the current directory
        for file in files:
            local_file = os.path.join(root, file)
            remote_file = f"{ftp_path}/{file}"
            with open(local_file, "rb") as f:
                ftp.storbinary(f"STOR {remote_file}", f)
            print(f"Uploaded: {remote_file}")

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
        ftp.set_debuglevel(0)
        ftp.login(config["ftp_user"], config["ftp_pwd"])
        ftp.set_pasv(True)
        print(f"Connected to FTP: {config['ftp_host']}")

        # Change to target directory
        if "ftp_target_dir" in config and config["ftp_target_dir"]:
            ftp.cwd(config["ftp_target_dir"])
            print("Changed to target directory:", ftp.pwd())
        else:
            print("Current directory:", ftp.pwd())

        list_directory(ftp)

        # Upload directory
        local_dir_path = "myproject/templates"  # <-- Set your local directory path here
        remote_dir_path = ftp.pwd()             # Upload to current directory
        upload_directory(ftp, local_dir_path, remote_dir_path)

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
