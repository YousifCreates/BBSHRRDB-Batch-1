print(f"{"Task 1: Write a Python program that takes a temperature value from the user and checks whether the weather is cold, normal, or hot.":^50}")
ask = float(input("Enter the temperature value: "))
if ask < 0:
    print("The weather is cold.")
elif ask > 30:
    print("The weather is hot.")
else:
    print("The weather is normal.")