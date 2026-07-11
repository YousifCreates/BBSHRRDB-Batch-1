dic = {"name" : "sadia",
       "age" : 20,
       "city" : "hyd",
       "dept" : "AI"}
print(dic) 

mark = {"English" : 86,
        "Math" : 79,
        "Physics" : 90}
for value in mark.values():
    print(value)

student = {"name" : "ayesha",
           "F/name" : "M.Jawaid"}
student.update({"semester" : 8})
print(student)

marks = {"Math" : 89,
       "AI" : 95,
       "English" : 79}
marks["English"] = 85
print(marks)

self = {"name" : "fatima",
        "age" : 17,
        "district": "hyd"}
self.pop("age")
print(self)


student = {"name" : "fatima",
        "age" : 17,
        "district": "hyd"}    
print(student.keys())

fruit = {"Apple" : 5,
         "banana" : 6,
         "Mango" : 8}
print(fruit.values())
print(fruit.items())

skin_care = {"Lipstick" : 500,
             "Eyeliner" : 250,
             "Mascara" : 300,
             "foundation" : 1000}
print(sum(skin_care.values()))

marks = {"Math" : 89,
        "AI" : 95,
        "English" : 79,
        "statistic" : 92}
print("Highest mark: ", max(marks.values()))
print("Lowest mark: ", min(marks.values()))


students = {
    "student1" :{
        "name" : "muskan",
        "age " : 21,
        "dept" : "AI",
        "semester" : 6,
    },
    "student2" :{
        "name" : "ayesha",
        "age" : 20,
        "dept" : "MLT"
    },
    "student3" :{
        "name" : "fadia",
        "age" : 24,
        "dept" : "IT"
    }
}

print(students)

student1 ={
        "name" : "muskan",
        "age " : 21,
        "dept" : "AI",
        "semester" : 6,
    }
if "name" in student1:
    print("Exist name in student2")
else:
    print("Not exist!")


student_data = {
        "name" : "ayesha",
        "age" : 20,
        "dept" : "MLT"
    }
print(student_data.clear())

name = ["sadia ", "ayesha", "Mahnoor"]
marks = [89, 90,79]

studdent = dict(zip(name, marks))
print(studdent)

list1 = [1,1,1,2,2,3,3,3,3,4]
freq_dict = {}

for element in list1:
    if element in freq_dict:
        freq_dict[element] = freq_dict[element] + 1
    else:
        freq_dict[element] = 1

print(freq_dict)

