import smtplib
import ssl
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from html_template import html

# LOAD ENVIRONMENT VARIABLES
load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
smtp_server = os.getenv("SMTP_SERVER")
port = os.getenv("PORT")

# STUDENT INFORMATION

receiver = "2k24-ai-60@usindh.edu.pk"

student_name = "Muhammad Yousif"
course_name = "AI Automation & Robotics"
registration_id = "BBSHRRDB-2026-00125"
registration_date = "20 August 2026"
venue = "University of Sindh, Jamshoro"

# EMAIL SUBJECT
subject = "Registration Successful — BBSHRRDB"
message = MIMEMultipart("alternative")

message["Subject"] = subject
message["From"] = email
message["To"] = receiver

# PLAIN TEXT VERSION
text = f"""
BBSHRRDB — Registration Successful

Hello {student_name},

Congratulations!

Your registration for the BBSHRRDB {course_name} program has been successfully completed.

Registration Details:

Name: {student_name}
Program: {course_name}
Registration ID: {registration_id}
Registration Date: {registration_date}
Venue: {venue}

Please keep your Registration ID for future reference.

You will receive further information regarding classes, schedule,
and other important instructions from the BBSHRRDB team.

Regards,
BBSHRRDB Team

Benazir Bhutto Shaheed Human Resource Research & Development Board
"""



# ATTACH BOTH VERSIONS


message.attach(MIMEText(text, "plain", "utf-8"))
message.attach(MIMEText(html, "html", "utf-8"))



# SEND EMAIL


context = ssl.create_default_context()

try:

    with smtplib.SMTP_SSL(
        smtp_server,
        port,
        context=context
    ) as server:

        server.login(email, password)

        server.sendmail(
            email,
            receiver,
            message.as_string()
        )

    print("Email sent successfully!")

except smtplib.SMTPAuthenticationError:

    print("SMTP authentication failed.")
    print("Please check your email and password.")

except smtplib.SMTPServerDisconnected:

    print("SMTP server unexpectedly closed the connection.")

except Exception as e:

    print(f"An error occurred: {e}")