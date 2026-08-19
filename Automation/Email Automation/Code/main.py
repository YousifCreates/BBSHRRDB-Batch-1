from dotenv import load_dotenv
import os
import ssl
import smtplib
from email.message import EmailMessage

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
port = int(os.getenv("PORT"))
smtp_server = os.getenv("SMTP_SERVER")

context = ssl.create_default_context()
msg = EmailMessage()
# """
#  {
#      "From":"{email}",
#      "To":"{email}",
#      "Subject":"Test Email",
#     }
#
# # """

subject = "Hello, This is automated email from Python!"
body = """
        This is line 1. \n
        This is line 2. \n
        This is line 3. \n
        This is line 4. \n

"""

receiver_email = "yousifcreates@gmail.com"
msg["From"] = email
msg["To"] = receiver_email
msg["Subject"] = subject
msg.set_content(body)

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(email, password)
    print("Logged in successfully!")
    server.send_message(msg)
    print("Message sent successfully!")