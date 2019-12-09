number = int(input("Enter a number: "))

total = 0

for i in range(1, number, 2):
    total = total + i

print(total)