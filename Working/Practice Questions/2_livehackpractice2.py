average = int(input("Enter the average: "))

money_earned = int(input("Enter the amount of money earned: "))

if average >= 80 and money_earned >= 500:
    print("Congratulations! You can go to Europe!")
elif average >= 80 and money_earned < 500:
    print("Congratulations! You can go to California!")
else:
    print("Congratulations! You can stay home!")



