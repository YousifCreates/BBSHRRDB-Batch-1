print(f"{"Task 5:  Comprehensive Text Analysis":^50}")
ask = input("Enter a text to analyze: ")
uppercase = ask.upper()
total = len(ask)
count = ask.count("e")
if ask.split()[0] == "The":
    a = "True"
else:
    a = "False"

print(f'''Text Analysis Results:
- Uppercase: {uppercase}
- Total Characters: {total}
- Count of 'e': {count}
- Starts with 'The': {a}''')