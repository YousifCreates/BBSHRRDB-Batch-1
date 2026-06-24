# def display_message():
#     print("Python is Fun!")
#
# display_message()
from strings import name


# n = input("What is your name? ")
# def greet(name):
#     print(f"Hello {name}, welcome to Python!")
# greet(n)

# def add(num_1, num_2):
#     result = num_1 + num_2
#     return result
#
# addition_res = add(15, 10)
#
# def subtract(num_1, num_2):
#     result = num_2 - num_1
#     return result
# subtract_res = subtract(15, 10)


# Default parameter values
# def greet(name="Guest"):
#     print(f"Hello {name}, Welcome back!")
# greet("10")

# def student_info(name, age, department = "Artificial Intelligence"):
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#     print(f"Department: {department}")
#
# student_info(age = 25, name = "Yousif")

# def addition(*numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     return total
#
# # print(addition(1, 2, 3))
#
# number_list = []
# while True:
#     user_input = input("Enter a number or type 'exit' to end: ")
#     if user_input.lower() == 'exit':
#         break
#     else:
#         number = float(user_input)
#         number_list.append(number)
#
# number_tuple = tuple(number_list)
# print(addition(*number_tuple))



def student_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

student_info(name="Krish", age=22, cnic=416010000000052, department="Robotics")
student_info(name="Yousif", phone="+92333000256852")










