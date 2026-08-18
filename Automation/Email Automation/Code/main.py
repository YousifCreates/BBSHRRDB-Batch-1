from dotenv import load_dotenv
import os
import ssl
import smtplib

# .\venv\Scripts\activate

load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
port = os.getenv("PORT")
smtp_server = os.getenv("SMTP_SERVER")

context = ssl.create_default_context()

# Login Logic
with smtplib.SMTP(smtp_server, port) as server:
    server.login(email, password, context=context)
    print("Logged in")