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
        pass
    with open("students_info.txt", "a") as file:
        file.write(f"{name},{username},{email},{password}\n")
        print("Credentials saved, Please login to continue.")
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