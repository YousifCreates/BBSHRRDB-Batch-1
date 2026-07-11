
# students = [
#     ("Ali", 80),
#     ("Sara", 95),
#     ("Ahmed", 70),
#     ("Ayesha", 88)
# ]

# sorted_students = sorted(students, key=lambda x: x[1])

# print(sorted_students)

# Program 7

# num = int(input("Enter a number: "))
# def analyze_number(number):
#     if number > 0:
#         return "Positive"

#     elif number < 0:
#         return "Negative"

#     else:
#         return "Zero"
# print(analyze_number(num))
 
        #  Program 8
# def even_odd(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# num = int(input("Enter a number: "))
# print(even_odd(num))


# def rectangle_area(length, width):
#     return length * width

# length = float(input("Enter length: "))
# width = float(input("Enter width: "))

# print("Area =", rectangle_area(length, width))


# def largest(a, b, c):
#     return max(a, b, c)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# print("Largest number =", largest(a, b, c))


# def average(a, b, c, d, e):
#     return (a + b + c + d + e) / 5

# num1 = float(input("Enter number 1: "))
# num2 = float(input("Enter number 2: "))
# num3 = float(input("Enter number 3: "))
# num4 = float(input("Enter number 4: "))
# num5 = float(input("Enter number 5: "))

# print("Average =", average(num1, num2, num3, num4, num5))

# def is_prime(number):
#     if number <= 1:
#         return False

#     for i in range(2, number):
#         if number % i == 0:
#             return False

#     return True

# num = int(input("Enter a number: "))

# if is_prime(num):
#     print("Prime Number")
# else:
#     print("Not a Prime Number")

#     program 10

# def count_vowels(text):
#     vowels = "aeiouAEIOU"
#     count = 0

#     for letter in text:
#         if letter in vowels:
#             count += 1

#     return count

# sentence = input("Enter a string: ")
# print("Total vowels =", count_vowels(sentence))

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1

#     return n * factorial(n - 1)

# num = int(input("Enter a number: "))

# print("Factorial =", factorial(num))



def fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter a number: "))

print("Fibonacci =", fibonacci(num))



# numbers = [1, 2, 3, 4, 5]

# result = list(map(lambda x: x * 2, numbers))

# print(result)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# odd = list(filter(lambda x: x % 2 != 0, numbers))

# print(odd)

# num = [1, 2, 3, 4,5 ,6, 7, 8,9, 10]
# even = list(filter(lambda x : x%2 == 0, num))
# print(even)