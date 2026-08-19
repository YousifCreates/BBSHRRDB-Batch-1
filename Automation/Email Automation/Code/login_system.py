from dotenv import load_dotenv
import os
import ssl
import smtplib
from email.message import EmailMessage

load_dotenv()
sender_email = os.getenv("EMAIL")
sender_password = os.getenv("PASSWORD")
port = int(os.getenv("PORT"))
smtp_server = os.getenv("SMTP_SERVER")
context = ssl.create_default_context()


subject = "You have signed up successfully at BBSHRRDB!"
body = f"""
        Hello, This is an automated email from BBSHRRDB Student Portal! \n
        You have successfully signed up at BBSHRRDB Student Portal. \n
        Thank you for signing up! \n
        Regards, \n
        BBSHRRDB Student Portal Team \n

        """



# Sign up function

def signup():
    print("=== Sign up ===")
    name = input("Enter your full name: ")
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    try:
        with open("students_info.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 4 and username == username:
                    print("Username taken, please choose a different username.")
                    return
    except FileNotFoundError:
        print("File not found, creating a new file.")
    with open("students_info.txt", "a") as file:
        file.write(f"{name},{username},{email},{password}\n")
        print("Credentials saved, Please login to continue.")
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, sender_password)
        print("Logged in successfully!")
        msg = EmailMessage()
        msg["From"] = sender_email
        msg["To"] = email
        msg["Subject"] = subject
        msg.set_content(body)
        server.send_message(msg)
        print("Message sent successfully!")
    return

# Login function:
def login():
    print("=== Login ===")
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")
    try:
        with open("students_info.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                name, username, email, password = data
                if len(data) == 4 and username_input == username:
                    if password_input == password:
                        print("=== Login Successful ===")
                        print(f"Name: {name}")
                        print(f"Username: {username}")
                        print(f"Email: {email}")
                        return
                    else:
                        print("Incorrect Password")
                        return
                else:
                    print("Username not found, please sign up to continue with that username.")
    except FileNotFoundError:
        pass


# Main function:
if __name__ == "__main__":
    file = open("students_info.txt", "a")
    file.close()
    print("*** Welcome to the BBSHRRDB Student Portal ***")
    while True:
        print("Select a Choice to continue:\n1. Signup\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            signup()
            continue
        if choice == "2":
            login()
            continue
        if choice == "3":
            print("Goodbye, Take Care")
            break
        else:
            print("Invalid Choice")