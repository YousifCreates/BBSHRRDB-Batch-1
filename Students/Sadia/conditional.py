# number = 6
# if number >= 10:
#     print("Positive")
# elif number <=0 :
#     print("negative")   
# else:
#     print("zero") 

# marks = float(input("Enter the marks:"))
# if marks >= 85:
#     print("A")
# elif marks >= 75:
#     print("B")
# elif marks >=65:
#     print("C")
# else:
#     print("Fails")


# years = int(input("Enter the year: "))
# if (years % 4 == 0 and years % 100 != 0) or (years % 400 == 0):
#     print("This is a leap year")
# else:
#     print("This is not leap year")


# a = int(input("enter first no:"))
# b = int(input("enter second no:"))
# c = int(input("enter third no:"))

# if (a >= b) and (a >= c):
#     print("The largest no is a:", a)
# elif (b >= a) and (b >= c):
#     print("The largest no is b:", b)
# else:
#     print("The largest no is c:", c)

age = int(input("Enter the age: "))
if age >= 30:
    print("Senior citizen")
elif age >= 18:
    print("Adult")
elif age > 10 or age < 18 :
    print("Teenage")
else:
    print("Child")