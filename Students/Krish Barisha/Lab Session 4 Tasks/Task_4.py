print(f"{"Task 4: Parsing Email Domains":^50}")
ask = input("Enter an email address: ")
if "@" in ask:
    domain = ask.split("@")
    print(f"The domain of the email address is: {domain[1]}")
else:
    print("Invalid email address. Please include '@' in the address.")