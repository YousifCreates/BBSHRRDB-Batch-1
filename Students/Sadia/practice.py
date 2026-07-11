# student = ("John Doe", 20, "Computer Science")

# print("Name:", student[0])
# print("Age:", student[1])
# print("Major:", student[2])

# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("The year is a leap year.")
# else:
#     print("The year is not a leap year.")


# price = float(input("Enter product price: "))
# customer = input("Enter customer type (student/regular/other): ")

# if customer.lower() == "student":
#     discount = price * 0.20
# elif customer.lower() == "regular":
#     discount = price * 0.10
# else:
#     discount = 0

# final_price = price - discount

# print("Discount:", discount)
# print("Final Price:", final_price)


# my_list = [25, 65.3, 1, -5]
# my_list = []
# while True:
#     value = input("Enter a value: ")
#     if value.lower().strip() == "done":
#         break
#     my_list.append(value)

# print(my_list)

# n = int(input("Enter a number: "))
n = 5

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

# full diamond pattern
n = 5

# Top half
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Bottom half
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))


# n = 5

# for i in range(1, n + 1):
#     for j in range(i):
#         print(chr(65 + j), end=" ")
#     print()


# n = 5

# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# n = 5

# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     for j in range(1, i + 1):
#         print(chr(64 + j), end=" ")
#     print()

n = 5

# Top half
for i in range(n):
    print(" " * (n - i - 1), end="")
    
    for j in range(i + 1):
        print(chr(65 + j), end="")
    
    for j in range(i - 1, -1, -1):
        print(chr(65 + j), end="")
    
    print()

# Bottom half
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1), end="")
    
    for j in range(i + 1):
        print(chr(65 + j), end="")
    
    for j in range(i - 1, -1, -1):
        print(chr(65 + j), end="")
    
    print()

    # sqaue empty 
n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


    # fill square 
    n = 5

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

# name = input("Enter your name: ")
# name_list = name.split(" ")
# length = 0
# for name in name_list:
#     length += len(name)

# print(length)

# x = 6
# print("Value:", x, "| Memory ID:", id(x))

# x = 10
# print("Value:", x, "| Memory ID:", id(x))

# x= y = 5
# print(id(x))
# print(id(y))
# print(id(x) == id(y))


# a = 50
# b = 80
# print("Before swapping: a =", a, "b =", b)
# a, b = b, a 
# print("After swapping: a =",a, "b =",b)

# count = 0
# # for i in range(1, 6):
# #     count += 1
# #     print("Count:", count)
# count +=1
# count +=1
# count +=1
# count +=1
# print("count:", count)

# temp = 36.6
# print(temp)

# temp = "fever"
# print(temp)

# item_name = "laptop"
# price = 12200.0
# quantity = 3

# total = price * quantity
# print(f"Item: {item_name}, Price: {price}, Quantity: {quantity}, Total: {total}")


# i = 10
# f = 3.14
# s = "hello"
# b = True
# l = [1, 2, 3]
# t = (4, 5, 6)
# d = {"key": "value"}
# n = None

# for val in [i, f, s, b, l, t, d, n]:
#     print(f"Value: {val!r} | Type: {type(val).__name__}")

# full_name = "sadia"
# print("Length:", len(full_name))
# print("Uppercase:", full_name.upper())
# print("Replaced:", full_name.replace("sadia", "Student"))
# print("'a' in name:", "a" in full_name)

# a = 7
# b = 2

# result_float = a / b
# result_int   = a // b

# print(f"{a} / {b}  = {result_float} ({type(result_float).__name__})")
# print(f"{a} // {b} = {result_int}   ({type(result_int).__name__})")

# student = {
#     "name": "Ali",
#     "age": 20,
#     "grade": "A",
#     "is_enrolled": True
# }

# for key, value in student.items():
#     print(f"{key}: {value!r} — Type: {type(value).__name__}")



# test_values = [0, 0.0, "", "0", [], {}, None, False]

# for val in test_values:
#     result = "Truthy" if bool(val) else "Falsy"
#     print(f"bool({val!r}) → {result}")


# f = 9.99
# i = int(f)   # Decimal part is TRUNCATED (not rounded) → 9
# print(f"float: {f}  →  int: {i}")  # 9.99 → 9

# s = str(f)
# print(f"As string: {s!r}  →  Type: {type(s).__name__}")  # '9.99' → str
# Cannot do arithmetic:
# print(s + 1)  # This would raise a TypeError

# n = (15, 9,10,7)
# for num in n:
#     print(f"Number: {num}")
#     if num % 3 == 0 and num % 5 == 0:
#         print(f"{num} is divisible by both 3 and 5")
#     elif num % 3 == 0:
#         print(f"{num} is divisible by 3")
#     elif num % 5 == 0:
#         print(f"{num} is divisible by 5")
#     else:
#         print(f"{num} is neither divisible by 3 nor by 5")


# secret = int(input("Enter the secret number (1-100): "))
# guess  = int(input("Enter your guess: "))

# if guess > secret:
#     print("Too High")
# elif guess < secret:
#     print("Too Low")
# else:
#     print("Correct!")

# Print a decorative animated-style title
# print("*" * 30)
# print("*" + " " * 28 + "*")
# print("*" + "   MY AWESOME ASCII ART   ".center(28) + "*")
# print("*" + " " * 28 + "*")
# print("*" * 30)




# print("A", "B", sep="---", end="!!!\n")