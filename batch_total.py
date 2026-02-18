total = 0
count = int(input("How many transactions? "))

for i in range(count):
    amount = float(input(f"Enter transaction {i+1}: "))
    total += amount

print(f"Total amount = {total}")
