decimal = int(input("Enter decimal number: "))
binary = bin(decimal)[2:]
hexa = hex(decimal)[2:].upper()

print("+--------------------+-------------------+---------+")
print(f"| {'DECIMAL':<18} | {'BINARY':<17} | {'HEX':<7} |")
print("+--------------------+-------------------+---------+")
print(f"| {decimal:<18} | {binary:<17} | {hexa:<7} |")
print("+--------------------+-------------------+---------+")