import psutil
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# ---------- Configuration ----------
RAM_THRESHOLD = 50  # percentage
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"  # use an App Password, not your real password
RECEIVER_EMAIL = "receiver_email@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587


# ---------- Function to send email ----------
def send_alert_email(ram_usage):
    subject = "⚠ High RAM Usage Alert"
    body = f"RAM usage crossed the threshold!\n\nCurrent Usage: {ram_usage}%\nTime: {datetime.now()}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()
        print("Alert email sent successfully.")
    except Exception as e:
        print("Failed to send email:", e)


# ---------- Main Logic ----------
def check_ram_usage():
    ram_usage = psutil.virtual_memory().percent
    print(f"Current RAM Usage: {ram_usage}%")

    if ram_usage > RAM_THRESHOLD:
        send_alert_email(ram_usage)


if __name__ == "__main__":
    check_ram_usage()