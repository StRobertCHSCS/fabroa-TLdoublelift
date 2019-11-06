# get the lengths from user
first_number = float(input("Enter the first side length: "))

second_number = float(input("Enter the second side length: "))

third_number = float(input("Enter the third side length: "))

first_calculation = first_number**2 + second_number**2

second_calculation = third_number**2

if first_calculation == second_calculation:
    print("You have a right triangle!")
else:
    print("You do not have a right triangle, idiot.")
