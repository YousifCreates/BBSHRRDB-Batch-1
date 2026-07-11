# list1 = [12, 32, 43, 54, 65, 76, 87, 98]
# sum = 0
# maximum = list1[0]
# minimum = list1[0]
# for num in list1:
#     sum += num
#     if num > maximum:
#         maximum = num
#     if num < minimum:
#         minimum = num
# print("Sum of elements in the list:", sum)
# print("Maximum element in the list:", maximum)
# print("Minimum element in the list:", minimum)

# my_list = [1, 2, 3, 4, 4, 3]
# print("Original list:", my_list)
# print("Unique elements:", list(set(my_list)))

# fruites = ("apple", "mango", "kiwi", "cherry", "orange")
# fruites[0] = "banana"  # This will raise an error because tuples are immutable
# print(fruites)

# vegetables = ("carrot", "broccoli", "spinach", "cauliflower")
# new_vegetables = vegetables + ("tomato",)
# # vegetables[0] = "tomato"  # This is valid because lists are mutable
# print(vegetables)
# print(new_vegetables)


# student = {
#     "ayesha" : 80,
#     "faiza" : 90,
#     "mahnoor" : 76
# }
# student["fadia"] = 85
# print(student)
 
students = {{
        "name" : "ayesha",
        "age" : 22,
        "marks" : 87},{
        "name" : "Fadia",
        "age" : 20,
        "mark " : 91},
        {"name" : "Mahnoor",
        "age" : 16,
        "marks" : 78}
}
for std in students:
    print("Name: ", std["name"])
    print("Age: ", std["age"])
    print("Marks: ", std["marks"])
    print()