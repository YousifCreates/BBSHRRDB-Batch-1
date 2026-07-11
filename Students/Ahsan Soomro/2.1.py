# #Task 1: The Classic Welcome Banner 
# #Objective: Use string multiplication to create a dynamic, scalable border around a welcome message. 
# print("========================================= ")
# print("=   WELCOME TO PYTHON PROGRAMMING LAB   =") 
# print("========================================= ")



a = "====================================="
print(len(a))
message = "WELCOME TO PYTHON PROGRAMMING LAB"
print(len(message))
border = "=" * (len(message) + 4 )

print(border)
print(f"= {message} =")
print(border)