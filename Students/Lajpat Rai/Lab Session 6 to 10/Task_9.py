# Task 9: Create a tuple of fruits. Convert it into a list, change one fruit, and convert it back into a tuple. 

print("\nTask 9: Create a tuple of fruits. Convert it into a list, change one fruit, and convert it back into a tuple.\n")
fruits = ('banana','apple','kiwi','papaya','pomgenerate')
fruits = list(fruits)
fruits[0] = 'Guava'
fruits = tuple(fruits)
print(fruits)