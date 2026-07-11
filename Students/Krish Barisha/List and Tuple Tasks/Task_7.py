# Task 7: Create a tuple with repeated values. Use count() to find how many times a specific value appears. 

print("\nTask 7: Create a tuple with repeated values. Use count() to find how many times a specific value appears.\n")
ran_nums = (12,12,12,12,12,33,34,34,34,5,5,67,76,8,4,4,4,4,5,57,7,8,8,7,87,8,78,78,788,78,787,87)

while True:
    ask = int(input("Enter a number to count: "))
    if ask in ran_nums:
        print("Number Found")
        counting = ran_nums.count(ask)
        print(f"The number is: {counting} Times present")
        try_again = input("Do you want to continue YES/NO: ")
        if try_again.lower().strip() == 'no':
            break
    else:
        print("Number not Found")
        re = input("Do you want to continue YES/NO: ")
        if try_again.lower().strip() == 'no':
            break
