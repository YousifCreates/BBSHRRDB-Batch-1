# my_list = [25, 65.3, 1, -5]
# # my_list.append("abc")
# print(my_list)
# # inser()
# # my_list.insert(2, "banana")
# # my_list.clear()
# # my_list.reverse()
# # my_list.remove(65.3)
# sorted_list = my_list.sort(reverse=True)
# print(my_list)


my_list = []
while True:
    value = input("Enter a value: ")
    if value.lower().strip() == "done":
        break
    my_list.append(value)

print(my_list)






