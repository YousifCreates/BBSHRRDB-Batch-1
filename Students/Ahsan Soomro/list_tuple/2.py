import random
numbers = [random.randrange(0, 100) for i in range(20)]

print(numbers)

odd = []
for i in range(0, len(numbers)):
    if numbers[i] %2 == 0:
        continue
    else:
        odd.append(numbers[i])


odd.sort()
print(odd)