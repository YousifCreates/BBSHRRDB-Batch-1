print(f"{"Task 3: Palindrome Verification":^50}")
ask = input("Enter a word or phrase to check if it's a palindrome: ")
if ask == ask[::-1]:
    print(f'"{ask}" is a palindrome.')
else:
    print(f'"{ask}" is NOT a palindrome.')