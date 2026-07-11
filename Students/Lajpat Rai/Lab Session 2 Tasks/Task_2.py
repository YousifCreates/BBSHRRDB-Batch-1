item1 = input("Enter item 1: ")
price1 = float(input("Enter price 1: "))

item2 = input("Enter item 2: ")
price2 = float(input("Enter price 2: "))

item3 = input("Enter item 3: ")
price3 = float(input("Enter price 3: "))

total = price1 + price2 + price3

print("-" * 57)
print(f"|{'RETAIL RECEIPT':^55}|")
print("-" * 57)

print(f"| {item1:<30} $ {price1:>20} |")
print(f"| {item2:<30} $ {price2:>20} |")
print(f"| {item3:<30} $ {price3:>20} |")

print("-" * 57)
print(f"| {'TOTAL:':<30} $ {total:>20} |")
print("-" * 57)