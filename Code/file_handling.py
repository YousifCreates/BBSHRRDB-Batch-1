# file = open("information.txt", "a")
# file.write("\nThird time")
# file.write("This is fourth time. \n")
# file.write("Fifth Time")
# file.close()
# file = open("information.txt", "r")
# content = file.read()
# print(content)
# file.close()
#


with open("informations.txt", "a") as file:
    file.write("Hello World")
    file.write("\n Second line")

with open("informations.txt", "r") as file:
    content =  file.read()
    print(content)