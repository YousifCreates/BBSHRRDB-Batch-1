# Task 3: Create a list of five student marks. Find the total, average, highest marks, and lowest marks. 

print("\nTask 3: Create a list of five student marks. Find the total, average, highest marks, and lowest marks.\n")
marks = [80,70,85,40,50]
total = 0
for i in range(0, len(marks)):
    total += marks[i]
length = len(marks)
avg = total/length
max_num = max(marks)
min_num = min(marks)
print(f"Total marks: {total}\nAverage: {avg}\nHighest Marks: {max_num}\nLowest Marks: {min_num}")