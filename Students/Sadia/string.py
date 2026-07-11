# text = input("Enter the string:")
# print(name.lower())
# print(name.upper())
# print(text.title())

msg = input("Enter the message: ")
count = 0
for char in msg:
    if char in "aeiouAEIOU":
        count += 1
print("Number of vowels:", count)

   

# text = text[::- 1]
# print(text)

# sentence = input("Enter the sentence: ")
# print(len(sentence), sentence.split(","))
# print(text.replace(" ", "_"))

# 

# print(sentence.startswith("i") and sentence.endswith("ad"))

text1 = input("Enter the word: ")
reverse_text = ""
for i in range (len(text1)-1, -1, -1):
    reverse_text += text1[i] 
print(reverse_text)



