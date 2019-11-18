'''
-------------------------------------------------------------------------------
Name:		livehack2_problem1.py
Purpose:	Determine the amount of bonus cash a class will receive based on average increase.

Author:	Lui.A

Created:	date in 18/11/2019
------------------------------------------------------------------------------
'''


#get the mid-term average and the final average of the class in percent

mid_average = float(input("Enter the class mid-term average in decimal form: "))

final_average = float(input("Enter the class final average in decimal form: "))

#calculate how much the average has improved from mid-term to finals

average_improvement = final_average - mid_average

#determine how much cash class will receive

if average_improvement >= 0.10:
    print("Congratulations, the cash bonus is $600.")
elif average_improvement >= 0.05:
    print("Congratulations, the cash bonus is $300.")
elif average_improvement >= 0.01:
    print("Congratulations, the cash bonus is $100.")
else:
    print("Sorry, no cash bonus for your class.")
    



