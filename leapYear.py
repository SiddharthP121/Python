
# Question 7 	Any year is input by the user. Write a program to determine whether the year is a leap year or not.

year = int(input("Enter the year to check wether it is a leap year \n"))

if year % 4 == 0:
    print("This year is a leap year\n")

else:
    print("This is not a leap year")    