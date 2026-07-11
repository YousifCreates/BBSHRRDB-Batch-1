# Task 6: Create a tuple of numbers. Find the sum, maximum value, minimum value, and length of the tuple. 

print("\nTask 6: Create a tuple of numbers. Find the sum, maximum value, minimum value, and length of the tuple.\n")
marks = (80,70,85,40,50)
total = 0
for i in range(0, len(marks)):
    total += marks[i]
length = len(marks)
max_num = max(marks)
min_num = min(marks)
print(f"Sum: {total}\nLength: {length}\nMax Value: {max_num}\nMin Value: {min_num}")