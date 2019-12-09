start = int(input("Enter the starting number: "))

end = int(input("Enter the ending number: "))

if start < end:
    for i in range(start, end + 1):
        print(i)
else:
    for i in range(start, end-1, -1):
        print(i)

