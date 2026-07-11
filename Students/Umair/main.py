from paramiko import file

filename = "notes.text"
note = ("input your today's note: ")

with open(filename "a") as file:
      file.write(note + "\n")

print("\n___All available notes ___")
with open(filename "r") as file:
     print(file.read




