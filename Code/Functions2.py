# # # def student_info(**info):
# # #     for key, value in info.items():
# # #         print(f"{key}: {value}")
# # #
# # # student_info(name="Krish", age=22, cnic=416010000000052, department="Robotics")
# # # student_info(name="Yousif", phone="+92333000256852")
# #
# #
# #
# # # number_list = []
# # # while True:
# # #     user_input = input("Enter a number: ")
# # #     if user_input.strip().lower() == "exit":
# # #         break
# # #     else:
# # #         number_list.append(user_input)
# # #
# # # print(number_list)
# #
# # message = "I am Global"
# # def print_local():
# #     message = "I am local"
# #     print(message)
# # =
# # print_local()
# # print(message)
#
#
#
#
#
#
#
#
#
# def countdown(n):
#     if n <= 0:
#         print("BlastOff")
#     else:
#         print(n)
#         countdown(n-1)
#


def square(x):
    return x*x

print(square(5))

square_lambda = lambda x:x * x
print(square_lambda(6))










