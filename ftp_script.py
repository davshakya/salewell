from ftplib import FTP_TLS
import ssl
import yaml

with open("config.yml", "r") as file:
    config = yaml.safe_load(file)

# Create a less strict SSL context
context = ssl.create_default_context()
context.set_ciphers("DEFAULT:@SECLEVEL=1")  # <-- allow small DH keys
ftp = FTP_TLS(context=context)
ftp.connect("ftpupload.net", 21)
ftp.login(config["ftp_user"], config["ftp_pwd"])
ftp.prot_p()  # Protect data connection
ftp.cwd("/salewell.co.in/htdocs")
with open("index.html", "rb") as file:
    ftp.storbinary("STOR index.html", file)
ftp.quit()
print("Upload successful.")
