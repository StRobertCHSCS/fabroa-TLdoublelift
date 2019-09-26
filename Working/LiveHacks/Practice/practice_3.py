minutes = int(input("enter amount of minutes: "))

days = str(minutes // 1440)
hours = str(minutes // 60)
minutes_left = str(minutes % 1440)

print("the time in days is: " + str(days))
print("the time of hours is: " + str(hours))
print("the minutes left: " + str(minutes_left))

