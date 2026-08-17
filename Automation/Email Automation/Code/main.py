import os
import ssl
import smtplib
from dotenv import load_dotenv

load_dotenv()

sender_email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
port = os.getenv("PORT")
smtp_server = os.getenv("SMTP_SERVER")

# SSL Connection
context = ssl.create_default_context()

# Login Logic:

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    print("Successfully Logged in")

