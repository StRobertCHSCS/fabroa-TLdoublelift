'''
-------------------------------------------------------------------------------
Name:		problem2.py
Purpose:	Pieces of chicken per student and remainder calculator 

Author:	Lui.A

Created:	date in 02/10/2019
------------------------------------------------------------------------------
'''

# get number of chicken pieces from user
chicken_pieces = int(input("Enter number of chicken pieces: "))

# get number of students 
students = int(input("Enter number of students: "))

# compute number of chicken pieces each student will get
chicken_per_student = chicken_pieces // students

# compute chicken left for Mr. Fabroa
chicken_left = chicken_pieces % students

# output number of chicken pieces per student and pieces left for Mr. Fabroa
print("each student will receive " + str(chicken_per_student) + " pieces")
print("There will be " + str(chicken_left) + " pieces left for Mr. Fabroa")
