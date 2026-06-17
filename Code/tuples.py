student = ("Looks Great", "25.3", 20, False, 36.2, True, 75, -69)
# # student[0] = 25 --Wrong
# print(type(student))
# #
# # tuple_2 = ("Value",25)
# # print(type(tuple_2))
#
# student_list = list(student)
# # student_list[0] = 25
# student = tuple(student_list)

for i in range(0, len(student) - 2, 2):
    print(student[i])


#print(student[2:])