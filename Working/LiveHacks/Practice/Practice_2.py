hours = int(input("amount of hours: "))

days = str(hours // 24)

print("hours converted to days: " + str(days))

hours_left = str(hours % 24)

print("hours converted into days: " + str(days) + " days and " + str(hours_left) + " hours")

