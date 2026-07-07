def recursive_sum(number):
    if number == 0:
        return 0
    return number + recursive_sum(number - 1)
print(recursive_sum(1))