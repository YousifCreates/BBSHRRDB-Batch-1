note = input("Enter the notes: ")

with open("notes.txt" , "a") as file:
    file.write(f"{note} \n")

with open("notes.txt", "r") as file:
    file.read()
print(note)



        



               
               