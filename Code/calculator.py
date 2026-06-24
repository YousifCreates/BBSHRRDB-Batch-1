def add(num_1, num_2):
    result = num_1 + num_2
    return result

def subtract(num_1, num_2):
    result = num_2 - num_1
    return result

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    if num_2 == 0:
        return "Divide by zero is not allowed"
    else:
        return num_1 / num_2



print("Select an operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
# print("5. Exit")

user_input = input("Select an operation (1-5): ")
num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))

if user_input == "1":
    print(add(num_1, num_2))
elif user_input == "2":
    print(subtract(num_1, num_2))
elif user_input == "3":
    print(multiply(num_1, num_2))
elif user_input == "4":
    print(divide(num_1, num_2))
else:
    print("Invalid operation")