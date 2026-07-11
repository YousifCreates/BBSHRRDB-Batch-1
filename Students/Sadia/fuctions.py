        # program1

# user_name = input("What's your name: ")
# def greet(name):
#     print(f"Hello {name}, welcome back in this course")

# greet(user_name)

        # program 2

# def sub(num1, num2):
#     result = num2 - num1
#     return result
# sub_result = sub(1, 10)
# print(sub_result)

        # program 3
# def add(num1, num2):
#     return num1 + num2

# def sub(num1, num2):
#     return num1 - num2

# def mul(num1, num2):
#     return num1 * num2

# def div(num1, num2):
#     if num2 == 0:
#         return "Divided by zero is not alllowed"
#     return num1 / num2

# while True:
#     print("Select an operation to perform:")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Exit")

#     user_input = input("Select an operation (1-5): ")

#     if user_input == "5":
#         print("Exiting the program...")
#         break

#     user_input = input("Select an operation (1-5): ")
#     if user_input == "5":
#       print("Exiting the program...")
#       break

#     num_1 = float(input("Enter first number: "))
#     num_2 = float(input("Enter second number: "))

#     if user_input == "1":
#         print(add(num_1, num_2))
#     elif user_input == "2":
#         print(sub(num_1, num_2))
#     elif user_input == "3":
#         print(mul(num_1, num_2))
#     elif user_input == "4":
#         print(div(num_1, num_2))
#     else:
#         print("Invalid input! Please select a valid operation.")

#     continue_this = input("Do you want to continue? (yes/no): ")

#     if continue_this.lower() != "yes":
#         print("Exiting the program...")
#         break

        # program 4
# def mark_grade(score):
#     if score >= 85:
#         return "A+"
#     elif score >= 80:
#         return "A"
#     elif score >= 70:
#         return "B"
#     elif score >= 60:
#         return "C"
#     else:
#         return "Fail"
    
# print(mark_grade(65))

        # program 5

# user_input = input("Enter your score: ")
# scores = float(user_input)

# def grade_marks(scores):

#     if scores >= 85:
#         return "A+"
#     elif scores >= 80:
#         return "A"
#     elif scores >= 70:
#         return "B"
#     elif scores >= 60:
#         return "C"
#     else:
#         return "Fail"
    
# print(grade_marks(scores))

        # program 6
# num = int(input("Enter a number: "))

# def square_no():
#     return num **2

# print(square_no())


# num = int(input("Enter the number: "))

# def no_analyze(no):
#     if no > 0:
#         return "Positive"
#     elif no < 0:
#         return "Negative"
#     else:
#         return "zero"
    
# print(no_analyze(num))


# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
# lambda_list = list(map(lambda x: x*2 , list1 ))
# odd = list(filter(lambda x: x%2 !=0 , list1))
# sorted_list = sorted(list1)
# print(lambda_list)
# print(odd)
# print(sorted_list)


# def prnt_lst(list, indx = 0):
#     if(indx == len(list)):
#         return
#     print(list[indx])
#     prnt_lst(list, indx +1)

# fruites = ["apple", "mango","kiwi", "cherry", "orange"]
# prnt_lst(fruites)


# n = int(input("Enter no: "))
# def fact(num):
#     if num==0 or num ==1:
#         return 1
#     else: 
#     return num * fact(num - 1)
# print(fact(n))


# n = int(input("Eneter the number: "))
# def sum_no(num):
#     if num == 0:
#         return 0
#     return num + sum_no(num - 1)

# print(sum_no(n))

# n = int(input("Enter no: "))
# def fib_series(num):
#     if num == 0:
#         return 0
    
#     if num == 1:
#         return 1
    
#     return fib_series(num - 1) + fib_series(num - 2)

# print(fib_series(n))

def is_prime(n):
    if n% 2 ==0 :
        return "false"
    return "Prime Number"
    
print(is_prime(2))