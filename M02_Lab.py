'''
M02 Lab - Case Study: if...else and while
M02_Lab.py
Author: Sophia Smith
Date: 3/27/2024
Summary: App will take user input name for student w/ their GPA then output if the stduent will make the Dean's List or Honor Roll
Version 1.0
'''

studentFirstName = " "
studentLastName = " "
studentGPA = 0.0


while True:
    studentFirstName = input("Enter Student First Name: ")
    studentLastName = input("Enter Student Last Name *Enter ZZZ to quit program*: ") 
    if studentLastName == 'ZZZ':
        break

    studentGPA = float(input("Enter Student GPA: "))

    if studentGPA >= 3.5:
        print("Congratulation ~ you made the Dean's List!")
        
    else:
        print("Sorry ~ you did not make the Dean's List")
        
    if studentGPA >= 3.25:
        print("Congratulation ~ you made the Honor Roll!")
       
    else:
        print("Sorry ~ you did not make the Honor Roll")
       
print("-" * 10)
print("~ Keep Up The Good Work ~")